from django.db import models
from django.conf import settings
from appartement.models import Appartement

class Favoris(models.Model):
     utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='mes_faoris')
     logement = models.ForeignKey(Appartement, on_delete=models.CASCADE, related_name='favoris')
     date_ajout = models.DateTimeField(auto_now_add=True)
     class Meta:
         unique_together = ('utilisateur', 'logement')
         def __str__(self):
             return f"{self.utilisateur.username}{self.logement.titre}"
         
             
# Create your models here.
