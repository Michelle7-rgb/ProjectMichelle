from django.db import models
from django.db import models
from django.conf import settings
from appartement.models import Appartement
from django.contrib.auth.models import User


class Conversation(models.Model):

    logement = models.ForeignKey(Appartement, on_delete=models.CASCADE)

    locataire = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='conversations_locataire'
    )

    proprietaire = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='conversations_proprietaire'
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id}"


class Message(models.Model):

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages'
    )

    expediteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    contenu = models.TextField()

    date_envoi = models.DateTimeField(auto_now_add=True)

    lu = models.BooleanField(default=False)

    def __str__(self):
        return f"Message de {self.expediteur.username}"
# Create your models here.
