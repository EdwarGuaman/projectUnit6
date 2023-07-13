from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):

    User = models.OneToOneField(User, on_delete=models.CASCADE)
    documento = models.PositiveBigIntegerField()
    direccion = models.CharField(max_length=50, default='')
    telefono = models.CharField(max_length=20, default='')

    def Usuario(self):
        return "{}, {} , {}, {}" .format(self.User.first_name, self.documento, self.direccion, self.telefono,  ) 
    
    def __str__ (self):
        return self.Usuario()
    
    


   

