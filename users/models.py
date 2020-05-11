from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address =  models.CharField(max_length=1024, default="none")
    isvet = models.BooleanField(default=False,null='True',blank='True')
    

    def __str__(self):
        return f'{self.user.username}'