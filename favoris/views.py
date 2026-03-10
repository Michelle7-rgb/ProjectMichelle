from django.shortcuts import render

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Favoris




@login_required
def mes_favoris(request):

    favoris = Favoris.objects.filter(utilisateur=request.user)

    return render(request, 'tenant_favorites.html', {
        'favoris': favoris
    })
# Create your views here.
