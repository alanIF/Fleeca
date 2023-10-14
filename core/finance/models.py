from django.db import models
from django.utils import timezone

from django.contrib.auth.models import (
    AbstractBaseUser,UserManager
)

class User(AbstractBaseUser):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    name = models.TextField()
    is_active= models.BooleanField(default=True)
    objects = UserManager()
    created = models.DateTimeField(default=timezone.now, editable=False)

    
class Type(models.Model):
    OPERATION_CHOICES = [
        ("+", "Sum"),
        ("-", "Subtract")
    ]
    name = models.TextField()
    operation  = models.CharField(max_length=1, choices=OPERATION_CHOICES)

    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Wallet(models.Model):
    name = models.TextField()
    creation_date = models.DateTimeField()
    created = models.DateTimeField(default=timezone.now, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)



class Moviment(models.Model):
    name = models.TextField()
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now, editable=False)
    value = models.FloatField()
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    