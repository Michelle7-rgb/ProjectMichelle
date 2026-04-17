from django.urls import path
from .views import envoyer_message, creer_conversation, voir_conversation, liste_conversations
urlpatterns = [
    path("m/",envoyer_message,name="messages"),
    path("conversation/<int:conversation_id>/", voir_conversation, name="voir_conversation"),
    path("conversations/", liste_conversations, name="liste_conversations"),
    path("conversations/nouveau/<int:logement_id>/", creer_conversation, name="creer_conversation"),
]

