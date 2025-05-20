from django.db import models
from django.utils.text import slugify

class ShowManager(models.Manager):
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)

class Show(models.Model):
    title = models.CharField("Titre du spectacle", max_length=200)
    slug = models.SlugField("Slug", max_length=200, unique=True, blank=True)
    description = models.TextField("Description", blank=True)
    
    prices = models.ManyToManyField(
        "catalogue.Price",
        related_name="shows",
        verbose_name="Tarifs"
    )

    objects = ShowManager()

    class Meta:
        db_table = "shows"
        verbose_name = "Spectacle"
        verbose_name_plural = "Spectacles"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.slug,)

    natural_key.dependencies = ['catalogue.price']