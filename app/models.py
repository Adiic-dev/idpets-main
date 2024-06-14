from django.db import models
from django.contrib.auth.models import User

class Mascota(models.Model):
    SEXO_CHOICES = [
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    ]
    
    TAMAÑO_CHOICES = [
        ('pequeño', 'Pequeño'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
    ]
    
    PELAJE_TIPO_CHOICES = [
        ('otro', 'Otro'),
        ('pelilargo', 'Pelilargo'),
        ('pelicorto', 'Pelicorto'),
    ]
    
    ESPECIE_CHOICES = [
        ('otro', 'Otro'),
        ('felino', 'Felino'),
        ('canino', 'Canino'),
    ]


    nombre = models.CharField(max_length=100, default='')
    especie = models.CharField(max_length=100, default='')
    raza = models.CharField(max_length=100, default='')
    sexo = models.CharField(max_length=6, choices=SEXO_CHOICES)
    edad = models.PositiveIntegerField()
    pelaje_color = models.CharField(max_length=100, default='')
    pelaje_tipo = models.CharField(max_length=100, choices=PELAJE_TIPO_CHOICES, default='')
    caracteristicas_distintivas = models.TextField(blank=True, null=True)
    tamaño = models.CharField(max_length=100, choices=TAMAÑO_CHOICES, default='')
    foto = models.ImageField(upload_to='fotos_mascotas/', blank=True, null=True)
    nombre_dueno = models.CharField(max_length=100, default='')
    numero_celular_dueno = models.CharField(max_length=8, default='+569')
    email_dueno = models.EmailField(null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"
