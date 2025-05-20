from django import forms
from catalogue.models.location import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["designation", "street", "number", "locality"]
        labels = {
            "designation": "Nom du lieu",
            "street": "Rue",
            "number": "Numéro",
            "locality": "Localité",
        }
        widgets = {
            "street": forms.TextInput(attrs={"placeholder": "Rue"}),
            "number": forms.TextInput(attrs={"placeholder": "Numéro"}),
        }
