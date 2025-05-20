from django.db import models

class Artist(models.Model):
    first_name = models.CharField("Prénom", max_length=100)
    last_name = models.CharField("Nom", max_length=100)

    class Meta:
        db_table = "artists"
        verbose_name = "Artiste"
        verbose_name_plural = "Artistes"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def natural_key(self):
        return (self.first_name, self.last_name)

    natural_key.dependencies = []