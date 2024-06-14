from django.contrib import admin
from .models import Mascota

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'sexo', 'edad', 'pelaje_color', 'pelaje_tipo', 'caracteristicas_distintivas', 'tamaño', 'foto', 'nombre_dueno', 'numero_celular_dueno', 'email_dueno')
    search_fields = ('nombre', 'especie', 'raza', 'nombre_dueno', 'numero_celular_dueno', 'email_dueno')

