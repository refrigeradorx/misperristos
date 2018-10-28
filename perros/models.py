from django.db import models 

OPCIONES_ESTADO = (
    ('1', 'Rescatado'),
    ('2', 'Disponible'),
    ('3', 'Adoptado'),
)

class Post(models.Model):
    Nombre = models.CharField(max_length=10)
    Raza = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=100)
    Fotografia = models.ImageField(upload_to='media')
    Estado = models.CharField(choices=OPCIONES_ESTADO, max_length=10,default=1)