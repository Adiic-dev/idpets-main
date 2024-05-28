from django.db import models

# Create your models here.


class Especie(models.Model):
    nombre = models.CharField(max_length=50)
    
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)  # Assuming raza is a string field
    SEXO_CHOICES = (
        ('M', 'Macho'),
        ('H', 'Hembra'),
        ('O', 'Otro'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    edad = models.IntegerField()  # Assuming edad is an integer field

class FichaMedica(models.Model):
    mascota = models.OneToOneField(Mascota, on_delete=models.CASCADE, related_name='ficha_medica')
    # Assuming you have other fields related to medical information
    archivos_pdf = models.FileField(upload_to='fichas_medicas/')