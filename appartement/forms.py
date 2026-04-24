from django import forms
from .models import Appartement, Signalement

class AppartementForm(forms.ModelForm):
    class Meta:
        model = Appartement
        fields = [
            'titre',
            'type_logement',
            'quartier',
            'prix',
            'description',
            'photo',
            'contact_proprietaire',
            'disponible',
        ]


class SignalementForm(forms.ModelForm):
    MOTIF_CHOICES = [
        ('spam', '🚫 Spam ou annonce inappropriée'),
        ('contenu_offensant', '⚠️ Contenu offensant ou illégal'),
        ('arnaque', '🔴 Possible arnaque ou fraude'),
        ('prix_anormal', '💰 Prix anormalement bas/haut'),
        ('autre', '❓ Autre raison'),
    ]

    motif = forms.ChoiceField(
        choices=MOTIF_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Motif du signalement'
    )

    class Meta:
        model = Signalement
        fields = ['details']
        widgets = {
            'details': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Expliquez le problème'}),
        }
