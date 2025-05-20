from django import forms
from catalogue.models import ReservationItem, Price

class ReservationItemForm(forms.ModelForm):
    # Champ visible pour l'affichage uniquement (non lié au modèle)
    display_price = forms.CharField(label="Tarif", required=False, disabled=True)

    class Meta:
        model = ReservationItem
        fields = ['price', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Récupérer l'objet Price si disponible dans initial
        price_obj = self.initial.get("price")

        if isinstance(price_obj, Price):
            # Cas de la création → price_obj est l’objet complet
            self.fields['display_price'].initial = f"{price_obj.type} – {price_obj.price:.2f} €"
            self.fields['price'].initial = price_obj.pk
        elif isinstance(price_obj, int):
            # Cas de l’édition → price_obj est juste l’ID
            try:
                price = Price.objects.get(pk=price_obj)
                self.fields['display_price'].initial = f"{price.type} – {price.price:.2f} €"
                self.fields['price'].initial = price.pk
            except Price.DoesNotExist:
                self.fields['display_price'].initial = "Tarif introuvable"
        else:
            self.fields['display_price'].initial = "Tarif inconnu"

        # Cache le champ price (mais il est présent dans le POST)
        self.fields['price'].widget = forms.HiddenInput()

        # Configure le champ quantity
        self.fields['quantity'].widget.attrs.update({'min': 0})
