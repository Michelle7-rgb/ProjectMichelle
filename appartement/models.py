from django.db import models
from django.conf import settings


class Appartement(models.Model):

    TYPE_CHOICES = [
        ('Studio', 'Studio'),
        ('Chambre', 'chambre'),
        ('T2', 'T2'),
        ('T3', 'T3'),
        ('Villa', 'Villa'),
         ('Appartement', 'Appartement'),
         ('Duplex', 'Duplex'),
    ]

    titre = models.CharField(max_length=50)
    type_logement = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )
    quartier = models.CharField(max_length=50)
    prix = models.PositiveIntegerField()
    description = models.TextField(max_length=500)

    photo = models.ImageField(
        upload_to='appartements/',
        blank=True,
        null=True,
    )

    proprietaire = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='appartements'
    )

    contact_proprietaire = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    

    def main_image(self):
     return self.images.filter(is_main=True).first()


    def __str__(self):
        return self.titre
    
class AppartementImage(models.Model):
    appartement = models.ForeignKey(
        Appartement,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='appartements/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"Image - {self.appartement.titre}"



class Favoris(models.Model): # Utilisez le singulier 'Favori' pour éviter les confusions
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='mes_coups_de_coeur' # Nom unique pour éviter le clash
    )
    appartement = models.ForeignKey(
        'Appartement', 
        on_delete=models.CASCADE,
        related_name='favorisé_par' # Nom unique ici aussi
    )
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('utilisateur', 'appartement')