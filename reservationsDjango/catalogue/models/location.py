from django.db import models
from catalogue.models import Locality

class LocationManager(models.Manager):
    def get_by_natural_key(self, designation, street, number, locality_postal, locality_name):
        return self.get(
            designation=designation,
            street=street,
            number=number,
            locality__postal_code=locality_postal,
            locality__locality=locality_name
        )

class Location(models.Model):
    designation = models.CharField("Désignation", max_length=100)
    street = models.CharField("Rue", max_length=100)
    number = models.CharField("Numéro", max_length=10)
    
    locality = models.ForeignKey(
        Locality,
        on_delete=models.RESTRICT,
        related_name="locations",
        verbose_name="Localité"
    )

    objects = LocationManager()

    class Meta:
        db_table = "locations"
        verbose_name = "Lieu"
        verbose_name_plural = "Lieux"
        ordering = ["designation"]

    def __str__(self):
        return f"{self.designation} – {self.street} {self.number}, {self.locality}"

    def natural_key(self):
        return (self.designation, self.street, self.number, *self.locality.natural_key())
    
    natural_key.dependencies = ['catalogue.locality']
