from django import forms
from catalogue.models import Representation


class RepresentationForm(forms.ModelForm):
    class Meta:
        model = Representation
        fields = ['show', 'when', 'location', 'capacity']
        widgets = {
            'when': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Format d'affichage pour le champ datetime
        if 'when' in self.fields:
            self.fields['when'].input_formats = ['%Y-%m-%dT%H:%M']
