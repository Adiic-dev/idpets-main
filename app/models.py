from django.db import models

from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    pelaje_color = models.CharField(max_length=100)
    pelaje_tipo = models.CharField(max_length=100)
    caracteristicas_distintivas = models.TextField()
    tamaño = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='mascotas/')
    nombre_dueno = models.CharField(max_length=100)
    numero_celular_dueno = models.CharField(max_length=15)
    email_dueno = models.EmailField(default='example@example.com')  # Establecer un valor por defecto

    def __str__(self):
        return self.nombre
