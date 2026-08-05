from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    #one to one relationship where one user is associated with one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE) #...CASCADE == if user is deleted, then delete all objects that reference to this profile
    
    def __str__(self): #allows you to print the variable
        return super().__str__()
