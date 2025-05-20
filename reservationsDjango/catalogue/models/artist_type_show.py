from django.db import models
from catalogue.models import Show, ArtistType

class ArtistTypeShow(models.Model):
    artist_type = models.ForeignKey(
        "ArtistType",
        on_delete=models.CASCADE,
        related_name="shows",
        verbose_name="Artiste + Type"
    )
    show = models.ForeignKey(
        "Show",
        on_delete=models.CASCADE,
        related_name="artist_type_links",
        verbose_name="Spectacle"
    )

    class Meta:
        db_table = "artist_type_show"
        verbose_name = "Participation artistique"
        verbose_name_plural = "Participations artistiques"
        unique_together = ("artist_type", "show")

    def __str__(self):
        return f"{self.artist_type} dans « {self.show.title} »"
