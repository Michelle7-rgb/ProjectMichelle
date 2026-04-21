from django.shortcuts import render, redirect
from django.db.models import Q

from .forms import RegisterForm
from favoris.models import Favoris
from message.models import Conversation, Message

# gestion de l'authentification

from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect('feed')
        else:
            messages.error(request, "Identifiants incorrects")

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  
            auth_login(request, user)  
            messages.success(request, "Compte créé avec succès !")
            return redirect('feed')
    else:
        form = RegisterForm()  

    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accueil')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profil(request):
    
    utilisateur = request.user

    conversations = Conversation.objects.filter(
        Q(locataire=utilisateur) | Q(proprietaire=utilisateur)
    )
    favoris_count = Favoris.objects.filter(utilisateur=utilisateur).count()
    messages_non_lus = Message.objects.filter(
        conversation__in=conversations,
        lu=False,
    ).exclude(expediteur=utilisateur).count()

    context = {
        "utilisateur": utilisateur,
        "favoris_count": favoris_count,
        "conversations_count": conversations.count(),
        "messages_non_lus": messages_non_lus,
    }

    return render(request, "tenant_profile.html", context)
