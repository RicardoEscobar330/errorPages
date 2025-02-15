from django.db import models

class Categoria(models.Model):
    #Atributos de la clase
    nombre = models.CharField(max_length=100) #Mandar a Construir un campo de los modelos de Django
    imagen = models.URLField()

    def __str__ (self):
        return self.nombre

# Create your models here.
