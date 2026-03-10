from django.urls import path
from .views import envoyer_message
urlpatterns = [
    path("m/",envoyer_message,name="messages"),
]

