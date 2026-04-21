from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.db.models import Count, Max, Q

from favoris.models import Favoris
from message.models import Conversation, Message
from .models import Appartement, AppartementImage

# gestion des vues pour l'application appartement

#accueil
def accueil(request):
    # Si l'utilisateur est connecté, redirige vers le feed
    if request.user.is_authenticated:
        return redirect('feed')

    # Sinon, affiche la page d'accueil publique
    appartements = Appartement.objects.filter(disponible=True).select_related('proprietaire').prefetch_related('images')
    return render(request, 'accueil.html', {'appartements': appartements})


# gestion des appartements
def ajouter_appartement(request):
    if not request.user.is_authenticated or request.user.role != 'PROPRIETAIRE':
        raise PermissionDenied

    if request.method == 'POST':
        appartement = Appartement.objects.create(
            titre=request.POST.get('titre'),
            type_logement=request.POST.get('type_logement'),
            quartier=request.POST.get('quartier'),
            prix=request.POST.get('prix'),
            description=request.POST.get('description'),
            proprietaire=request.user,
            contact_proprietaire=request.POST.get('contact'),
        )

        # images multiples
        for file in request.FILES.getlist('images'):
            AppartementImage.objects.create(
                appartement=appartement,
                image=file
            )

        return redirect('appartement_detail', pk=appartement.id)

    return render(request, 'owner_publish.html')

def supprimer_appartement(request, id):
    appartement = get_object_or_404(Appartement, id=id)

    if request.user != appartement.proprietaire and request.user.role != 'ADMIN':
        raise PermissionDenied

    appartement.delete()
    return redirect('feed')
 

def modifier_appartement(request, id):
    appartement = get_object_or_404(Appartement, id=id)

    if request.user != appartement.proprietaire and request.user.role != 'ADMIN':
        raise PermissionDenied

    if request.method == 'POST':
        appartement.titre = request.POST.get('titre')
        appartement.prix = request.POST.get('prix')
        appartement.description = request.POST.get('description')
        appartement.save()

        return redirect('appartement_detail', pk=appartement.id)

    return render(request, 'modifier_appartement.html', {'appartement': appartement})


def appartement_detail(request, pk):
    appartement = get_object_or_404(Appartement, pk=pk)
    images = [image for image in appartement.images.all() if image.image_url_safe]

    return render(request, 'appartement_detail.html', {
        'appartement': appartement,
        'images': images
    })

def liste_appartements(request):
    appartements = Appartement.objects.filter(disponible=True).select_related('proprietaire').prefetch_related('images')

    quartier = request.GET.get('quartier')
    type_logement = request.GET.get('type')
    prix_max = request.GET.get('prix')

    if quartier:
        appartements = appartements.filter(quartier__icontains=quartier)

    if type_logement:
        appartements = appartements.filter(type_logement=type_logement)

    if prix_max:
        appartements = appartements.filter(prix__lte=prix_max)

    context = {
        'appartements': appartements
    }
    return render(request, 'feed.html', context)

@login_required(login_url='login')
def feed(request):
    """
    Affiche la liste des appartements pour les utilisateurs connectés.
    Permet aux propriétaires de gérer leurs appartements.
    """

    # Récupérer tous les appartements disponibles
    appartements = Appartement.objects.filter(disponible=True).select_related('proprietaire').prefetch_related('images')

    # --- FILTRAGE ---
    quartier = request.GET.get('quartier')
    type_logement = request.GET.get('type')
    prix_max = request.GET.get('prix')

    if quartier:
        appartements = appartements.filter(quartier__icontains=quartier)
    if type_logement:
        appartements = appartements.filter(type_logement=type_logement)
    if prix_max:
        try:
            prix_max = float(prix_max)
            appartements = appartements.filter(prix__lte=prix_max)
        except ValueError:
            pass  # ignore si mauvais format

    recent_messages = []
    mes_favoris = []

    if request.user.is_authenticated:
        mes_favoris = (
            Favoris.objects.filter(utilisateur=request.user)
            .select_related('logement', 'logement__proprietaire')
            .order_by('-date_ajout')[:3]
        )
        recent_messages = (
            Message.objects.filter(Q(conversation__locataire=request.user) | Q(conversation__proprietaire=request.user))
            .select_related('conversation', 'conversation__logement', 'expediteur')
            .order_by('-date_envoi')[:3]
        )

    context = {
        'appartements': appartements,
        'mes_favoris': mes_favoris,
        'recent_messages': recent_messages,
    }

    return render(request, 'feed.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from favoris.models import Favoris

User = get_user_model()

@login_required
def dashboard_locataire(request):
    mes_favoris = Favoris.objects.filter(utilisateur=request.user).select_related('logement').order_by('-date_ajout')
    favoris_disponibles = mes_favoris.filter(logement__disponible=True).count()
    messages_non_lus = Message.objects.filter(
        conversation__in=Conversation.objects.filter(Q(locataire=request.user) | Q(proprietaire=request.user)),
        lu=False,
    ).exclude(expediteur=request.user).count()
    return render(request, 'dashboard_locataire.html', {
        'favoris': mes_favoris,
        'favoris_count': mes_favoris.count(),
        'favoris_disponibles': favoris_disponibles,
        'conversations_count': Conversation.objects.filter(Q(locataire=request.user) | Q(proprietaire=request.user)).count(),
        'messages_non_lus': messages_non_lus,
    })

@login_required
def admin_dashboard(request):
    total_users = User.objects.count()
    total_annonces = Appartement.objects.count()
    annonces_recentes = Appartement.objects.select_related('proprietaire').order_by('-date_publication')[:5]
    return render(request, 'admin_dashboard.html', {
        'total_users': total_users,
        'total_annonces': total_annonces,
        'annonces_recentes': annonces_recentes,
    })

def message(request):
    return redirect('liste_conversations')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appartement 

@login_required
def dashboard_proprietaire(request):
    mes_appartements = Appartement.objects.filter(
        proprietaire=request.user
    ).select_related('proprietaire').prefetch_related('images').order_by('-date_publication')

    total = mes_appartements.count()
    disponibles = mes_appartements.filter(disponible=True).count()
    avec_images = mes_appartements.filter(images__isnull=False).distinct().count()
    
    return render(request, 'dashboard_proprietaire.html', {
        'appartements': mes_appartements,
        'total_appartements': total,
        'disponibles': disponibles,
        'avec_images': avec_images,
    })


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from appartement.models import Appartement
from django.contrib.auth import get_user_model
User = get_user_model()



@login_required
def dashboard_admin(request):
    total_users = User.objects.count()
    total_annonces = Appartement.objects.count()
    appartements_recentes = Appartement.objects.select_related('proprietaire').order_by('-date_publication')[:5]

    context = {
        'total_users': total_users,
        'total_annonces': total_annonces,
        'appartements_recentes': appartements_recentes,
    }

    return render(request, 'admin_review.html', context)

@login_required
def owner_listings(request):
    appartements = Appartement.objects.filter(proprietaire=request.user).select_related('proprietaire').prefetch_related('images').order_by('-date_publication')
    return render(request, "owner_listings.html", {
        'appartements': appartements,
        'total_appartements': appartements.count(),
        'disponibles': appartements.filter(disponible=True).count(),
        'indisponibles': appartements.filter(disponible=False).count(),
    })