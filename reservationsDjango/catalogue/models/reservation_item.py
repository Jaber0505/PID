from django.db import models
from .reservation import Reservation
from .price import Price

class ReservationItemManager(models.Manager):
    def get_by_natural_key(self, reservation_natural_key, price_type):
        return self.get(
            reservation__user__username=reservation_natural_key[0],
            reservation__representation__show__slug=reservation_natural_key[1],
            reservation__representation__when=reservation_natural_key[2],
            price__type=price_type
        )

class ReservationItem(models.Model):
    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Réservation"
    )
    price = models.ForeignKey(
        Price,
        on_delete=models.RESTRICT,
        related_name="reservation_items",
        verbose_name="Tarif"
    )
    quantity = models.PositiveIntegerField(verbose_name="Quantité")

    objects = ReservationItemManager()

    def __str__(self):
        return f"{self.quantity} × {self.price.type} (Réservation {self.reservation.id})"

    def natural_key(self):
        return self.reservation.natural_key() + (self.price.type,)
    
    natural_key.dependencies = ['catalogue.reservation', 'catalogue.price']

    class Meta:
        db_table = "reservation_items"
        verbose_name = "Ligne de réservation"
        verbose_name_plural = "Lignes de réservation"
        unique_together = ("reservation", "price")
