from django.db import models
from django.conf import settings #acceder al conf de user
#app terceros
from model_utils.models import TimeStampedModel
#
from applications.entrada.models import Entry
# Create your models here.
from .managers import FavoritesManager
class Favorites(TimeStampedModel):
    """Modelo Favoritos"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_favorites', on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, related_name='entry_favorites', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'entry')
        verbose_name='Entrada Favorito'
        verbose_name_plural='Entradas Favoritos'
    
    objects = FavoritesManager()

    def __str__(self):
        return self.entry.title
