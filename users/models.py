from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image=models.ImageField(upload_to="users-avatar/",null=True,blank=True,verbose_name="Аватарка користувача")


