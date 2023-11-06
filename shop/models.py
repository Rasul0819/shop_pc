from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='media/users_images',blank=True)
    phone_num = models.CharField(blank=True,max_length=30)
