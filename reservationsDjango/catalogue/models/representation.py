from django.db import models
from .show import Show
from .location import Location


class RepresentationManager(models.Manager):
    def get_by_natural_key(self, show_slug, when):
        return self.get(show__slug=show_slug, when=when)

class Representation(models.Model):
    show = models.ForeignKey(
        Show,
        on_delete=models.RESTRICT,
        null=False,
        related_name='representations',
        verbose_name='Spectacle'
    )
    when = models.DateTimeField(
        verbose_name='Date et heure',
        help_text="Horaire de la représentation"
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.RESTRICT,
        null=True,
        related_name='representations',
        verbose_name='Lieu'
    )
    capacity = models.PositiveIntegerField(
        verbose_name='Capacité maximale',
        help_text="Nombre total de places disponibles pour cette représentation"
    )

    @property
    def places_restantes(self):
        total_reservations = sum(r.total_places_reserved() for r in self.reservations.all())
        return max(0, self.capacity - total_reservations)

    objects = RepresentationManager()

    def __str__(self):
        return f"{self.show.title} @ {self.when.strftime('%Y-%m-%d %H:%M')}"

    def natural_key(self):
        return (self.show.slug, self.when)
    
    natural_key.dependencies = ['catalogue.show', 'catalogue.location']

    class Meta:
        db_table = "representations"
        verbose_name = "Représentation"
        verbose_name_plural = "Représentations"
        constraints = [
            models.UniqueConstraint(
                fields=["show", "when"],
                name="unique_show_when"
            )
        ]
