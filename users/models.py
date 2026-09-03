from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image=models.ImageField(upload_to="users-avatar/",null=True,blank=True,verbose_name="Аватарка користувача")


