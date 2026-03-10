from django.urls import path
from .views import * #accueil, ajouter_appartement, feed, supprimer_appartement, modifier_appartement, appartement_detail,dashboard_locataire,dashboard_admin,message,dashboard_proprietaire

urlpatterns = [
    #path('log/', accueil, name='accueil'),
    path('', accueil, name='accueil'),
    path("feed/", feed, name="feed"),
    path("ajouter/", ajouter_appartement, name="owner_publish"),
    path("appartement/<int:pk>/", appartement_detail, name="appartement_detail"),
    path("appartement/<int:id>/modifier/", modifier_appartement, name="modifier_appartement"),
    path("appartement/<int:id>/supprimer/", supprimer_appartement, name="supprimer_appartement"),
    path("locataire/", dashboard_locataire, name="dashboard_locataire"),
    path("prop/",owner_listings , name="owner_listings"),
    path("ad/",dashboard_admin , name="admin_review"),
    path("me/", message, name="messages"),
    # path("prop/", dashboard_proprietaire, name="dashboard_proprietaire")
    
    
]



   # path('profile/', profile, name='profile'),
    



# Create your views here.
