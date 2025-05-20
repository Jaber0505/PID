from django import forms
from catalogue.models import Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['first_name', 'last_name', 'types']
        labels = {
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'types': 'Types d’artiste',
        }
        widgets = {
            'types': forms.CheckboxSelectMultiple()
        }
