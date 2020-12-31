# Create your models here.

# to implement a custom user model which the official Django documentation highly recommends.”5
#  Because you will need to make changes to the built-in User model at some point in your project’s life.


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):  #CustomUser now has inherited all the functionality of AbstractUser
    pass