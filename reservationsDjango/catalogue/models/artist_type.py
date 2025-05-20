from django.db import models
from catalogue.models import artist, type

class ArtistType(models.Model):
    artist = models.ForeignKey(
        "Artist",
        on_delete=models.CASCADE,
        related_name="artist_types",
        verbose_name="Artiste"
    )
    type = models.ForeignKey(
        "Type",
        on_delete=models.CASCADE,
        related_name="artist_types",
        verbose_name="Type"
    )

    class Meta:
        db_table = "artist_types"
        verbose_name = "Association artiste/type"
        verbose_name_plural = "Associations artiste/type"
        unique_together = ("artist", "type")

    def __str__(self):
        return f"{self.artist} ({self.type})"
