"""
Favorite Apartments Views
Handles user favorite apartments management.
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Favoris


@login_required
def mes_favoris(request):
    """
    Display all favorite apartments for current user.
    Shows recently added favorites first.
    """
    favoris = Favoris.objects.filter(
        utilisateur=request.user
    ).select_related('logement', 'utilisateur').order_by('-date_ajout')

    return render(request, 'tenant_favorites.html', {'favoris': favoris})
