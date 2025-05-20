from django.db import models
from catalogue.models.representation import Representation

from django.contrib.auth import get_user_model
User = get_user_model()

class ReviewManager(models.Manager):
    def get_by_natural_key(self, username, when, show_slug):
        return self.get(
            user__username=username,
            representation__when=when,
            representation__show__slug=show_slug
        )

class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Utilisateur"
    )
    representation = models.ForeignKey(
        Representation,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Représentation"
    )
    rating = models.IntegerField("Note", choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField("Commentaire", blank=True)

    objects = ReviewManager()

    class Meta:
        db_table = "reviews"
        verbose_name = "Avis"
        verbose_name_plural = "Avis"
        ordering = ["-representation__when"]

    def __str__(self):
        return f"{self.user.username} – {self.rating}/5"

    def natural_key(self):
        return (
            self.user.username,
            self.representation.when.isoformat(),
            self.representation.show.slug,
        )
    
    natural_key.dependencies = ['catalogue.representation', 'auth.user']
