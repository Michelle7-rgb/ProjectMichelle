from django.db import models
#from .models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ('PROPRIETAIRE', 'Met en vente/location'),
        ('CLIENT', 'Recherche un logement'),
        ('ADMIN', 'Gestionnaire de la plateforme'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='CLIENT'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"

    @property
    def phone(self):
        profile = getattr(self, 'profile', None)
        if profile and profile.phoneNuber:
            return profile.phoneNuber
        return ''
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    isOwner = models.BooleanField(default=False)
    phoneNuber = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
    
  

    
# Create your models here.
