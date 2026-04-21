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

    @property
    def photo_url_safe(self):
        if self.photo and self.photo.name and self.photo.storage.exists(self.photo.name):
            return self.photo.url
        return ""

    @property
    def primary_image_url(self):
        main = self.main_image()
        if main and main.image_url_safe:
            return main.image_url_safe

        for image in self.images.all():
            if image.image_url_safe:
                return image.image_url_safe

        return self.photo_url_safe


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

    @property
    def image_url_safe(self):
        if self.image and self.image.name and self.image.storage.exists(self.image.name):
            return self.image.url
        return ""

    def __str__(self):
        return f"Image - {self.appartement.titre}"