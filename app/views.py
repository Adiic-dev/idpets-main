from sqlite3 import IntegrityError
from django.contrib.auth import  authenticate
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from .forms import LoginForm
from django.contrib.auth import login as auth_login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm  # Agrega esta línea
from django.contrib import messages
from .forms import MascotaForm
from .models import Mascota
from django import forms

# Create your views here.

def inicio(request):
    return render (request, 'paginas/inicio.html')
def nosotros(request):
    return render (request,'paginas/nosotros.html')

def Mascotas(request):
    return render(request, 'Mascotas/Mascota.html')


@login_required
def registrar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.usuario = request.user  # Asocia la mascota con el usuario actual
            mascota.save()
            messages.success(request, '¡La mascota se registró correctamente!')
            return redirect('Mascotas')  # Cambia 'Mascotas' por la URL correspondiente
    else:
        form = MascotaForm()
    return render(request, 'Mascotas/registrar_mascota.html', {'form': form})



@login_required
def lista_mascotas(request):
    mascotas = Mascota.objects.filter(usuario=request.user)
    return render(request, 'Mascotas/Mascota.html', {'mascotas': mascotas})



def detalle_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    return render(request, 'mascotas/detalle_mascota.html', {'mascota': mascota})

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'


def editar_mascotas(request):
    return render(request, 'Mascotas/editar_mascotas.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Iniciar sesión automáticamente después del registro
            return redirect('inicio')  # Redirige a la página de inicio después de iniciar sesión
    else:
        form = CustomUserCreationForm()
    return render(request, 'paginas/signup.html', {"form": form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Iniciar sesión si las credenciales son válidas
                return redirect('inicio')
            else:
                # Mensaje de error si las credenciales son inválidas
                return render(request, 'paginas/login.html', {'form': form, 'error_message': 'Nombre de usuario o contraseña incorrectos'})
    else:
        form = LoginForm()
    return render(request, 'paginas/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)  # Cerrar sesión del usuario
    return redirect('login')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

@login_required
def editar_usuario(request):
    user = request.user
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        
        # Actualizar nombre de usuario si es diferente
        if nombre_usuario != user.username:
            user.username = nombre_usuario
            user.save()
        
        # Obtener la contraseña actual del formulario
        contraseña_actual = request.POST.get('contraseña_actual')
        
        # Verificar si la contraseña actual es válida antes de guardar los cambios
        if user.check_password(contraseña_actual):
            # Obtener el formulario de cambio de contraseña y validar
            password_change_form = PasswordChangeForm(user=user, data=request.POST)
            if password_change_form.is_valid():
                password_change_form.save()  # Guardar la nueva contraseña
                messages.success(request, 'Contraseña actualizada exitosamente.')
            else:
                for field in password_change_form:
                    for error in field.errors:
                        messages.error(request, f'{field.label}: {error}')
        else:
            messages.error(request, 'La contraseña actual es incorrecta.')

        return redirect('inicio')  # Redirigir a la página de inicio después de editar el perfil
    else:
        password_change_form = PasswordChangeForm(user=request.user)
        return render(request, 'editar_usuario.html', {'user': user, 'password_change_form': password_change_form})

    
@login_required
def borrar_usuario(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  # Eliminar el usuario
        return redirect('inicio')  # Redirigir a la página de inicio u otra página
    else:
        return render(request, 'borrar_usuario.html')