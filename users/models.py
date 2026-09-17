from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(
        upload_to="users-avatar/",
        null=True,
        blank=True,
        verbose_name="Аватарка користувача",
    )
    favorite_artists = models.ManyToManyField('artists.Artists',related_name='favorite_by',blank=True,verbose_name="Улюблені виконавці")
    favorite_releases = models.ManyToManyField('artists.Release',related_name='favorite_by',blank=True,verbose_name="Улюблені релізи")

