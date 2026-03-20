from django.urls import path
from .views import (
    accueil,
    feed,
    ajouter_appartement,
    appartement_detail,
    modifier_appartement,
    supprimer_appartement,
    owner_listings,
    dashboard_admin,
)

urlpatterns = [
    path('', accueil, name='accueil'),
    path("feed/", feed, name="feed"),
    path("ajouter/", ajouter_appartement, name="owner_publish"),
    path("appartement/<int:pk>/", appartement_detail, name="appartement_detail"),
    path("appartement/<int:id>/modifier/", modifier_appartement, name="modifier_appartement"),
    path("appartement/<int:id>/supprimer/", supprimer_appartement, name="supprimer_appartement"),
    path("prop/", owner_listings, name="owner_listings"),
    path("ad/", dashboard_admin, name="admin_review"),
]
