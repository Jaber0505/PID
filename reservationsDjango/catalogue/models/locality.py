from django.db import models

class LocalityManager(models.Manager):
    def get_by_natural_key(self, postal_code, locality):
        return self.get(postal_code=postal_code, locality=locality)

class Locality(models.Model):
    postal_code = models.CharField("Code postal", max_length=10)
    locality = models.CharField("Localité", max_length=100)

    objects = LocalityManager()

    class Meta:
        db_table = "localities"
        verbose_name = "Localité"
        verbose_name_plural = "Localités"
        ordering = ["postal_code", "locality"]
        unique_together = [("postal_code", "locality")]

    def __str__(self):
        return f"{self.postal_code} {self.locality}"

    def natural_key(self):
        return (self.postal_code, self.locality)

    natural_key.dependencies = []