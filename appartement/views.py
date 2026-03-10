from django.shortcuts import render
from .models import Appartement, AppartementImage
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# gestion des vues pour l'application appartement

#accueil
def accueil(request):
    # Si l'utilisateur est connecté, redirige vers le feed
    # if request.user.is_authenticated:
    #     return redirect('feed')

    # Sinon, affiche la page d'accueil publique
    appartements = Appartement.objects.filter(disponible=True)
    return render(request, 'accueil.html', {'appartements': appartements})


# gestion des appartements
from django.core.exceptions import PermissionDenied

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

    return render(request, 'ajouter_appartement.html')

def supprimer_appartement(request, id):
    appartement = get_object_or_404(Appartement, id=id)

    if request.user != appartement.proprietaire:
        raise PermissionDenied

    appartement.delete()
    return redirect('feed')
 

def modifier_appartement(request, id):
    appartement = get_object_or_404(Appartement, id=id)

    if request.user != appartement.proprietaire:
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
    images = appartement.images.all()

    return render(request, 'appartement_detail.html', {
        'appartement': appartement,
        'images': images
    })

def liste_appartements(request):
    appartements = Appartement.objects.filter(disponible=True)

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
    appartements = Appartement.objects.filter(disponible=True)

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

    # --- Gestion propriétaire ---
    proprietaire = request.user
    user_is_owner = hasattr(proprietaire, 'role') and proprietaire.role == 'PROPRIETAIRE'

    context = {
        'appartements': appartements,
        'user_is_owner': user_is_owner,
    }

    return render(request, 'feed.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Appartement, Favoris

User = get_user_model()

@login_required
def dashboard_locataire(request):
    # Utilisation du bon modèle de favoris et du bon champ de date
    mes_favoris = Favoris.objects.filter(utilisateur=request.user)
    return render(request, 'dashboard_locataire.html', {'favoris': mes_favoris})

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def message(request):
    return render(request, 'message.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appartement 

@login_required
def dashboard_proprietaire(request):
    # On récupère seulement les appartements de la personne connectée
    mes_appartements = Appartement.objects.filter(
        proprietaire=request.user
    ).order_by('-date_publication')
    
    return render(request, 'dashboard_proprietaire.html', {
        'appartements': mes_appartements
    })


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from appartement.models import Appartement
from django.contrib.auth import get_user_model
User = get_user_model()



@login_required
def dashboard_admin(request):
    
    # Compter les éléments importants
    total_users = User.objects.count()
    total_annonces = Appartement.objects.count()
    

    # Dernières annonces ajoutées
    Appartements_recentes = Appartement.objects.all().order_by('-date_publication')[:5]

    context = {
        'total_users': total_users,
        'total_Appartement': Appartement,
        'Appartement_recentes': Appartement,
    }

    return render(request, 'admin_review.html', context)

def owner_listings(request):
    return render(request, "owner_listings.html",{"active_view": "owner-listings"})