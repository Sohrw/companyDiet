from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_id = models.CharField(max_length=10)
    is_salad = models.BooleanField(default=False)
    choice_date = models.DateField(auto_now=True)

class Profile(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='images/')
    upload_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title