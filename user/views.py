import email
from django.shortcuts import render
from .models import User
from .forms import RegisterForm

# gestion de l'authentification

from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings



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
            return redirect('login')
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

    context = {
        "utilisateur": utilisateur
    }

    return render(request, "tenant_profile.html", context)
