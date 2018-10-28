from django.db import models 
from django.utils import timezone


class Post(models.Model):
    rut = models.CharField(max_length=10)
    nomCompleto = models.CharField(max_length=100)
    fecNac = models.DateTimeField()
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    region = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    vivienda = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, blank=False, null=False, default='M')

    def publish(self): 
        self.save()  #guarda los cambios en la bd

    def __str__(self): # lo mismo que toString
        return self.rut + ' - ' + self.nomCompleto + ' - ' + str(self.fecNac) + ' - ' + self.email + ' - ' + self.telefono + ' - ' + self.region + ' - ' + self.ciudad + ' - ' + self.vivienda
