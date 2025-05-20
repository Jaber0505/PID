from django import forms
from catalogue.models.show import Show

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ["title", "description", "prices"]
        labels = {
            "title": "Titre",
            "description": "Description",
            "prices": "Tarifs associés",
        }
        widgets = {
            "prices": forms.CheckboxSelectMultiple
        }
