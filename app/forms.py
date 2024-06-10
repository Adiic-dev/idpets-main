from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Mascota

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Nombre de Usuario')
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    
class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'mascota-form-input'}),
            'especie': forms.TextInput(attrs={'class': 'mascota-form-input'}),
            'raza': forms.TextInput(attrs={'class': 'mascota-form-input'}),
            'sexo': forms.Select(attrs={'class': 'mascota-form-input'}),
            'edad': forms.NumberInput(attrs={'class': 'mascota-form-input'}),
            'pelaje_color': forms.TextInput(attrs={'class': 'mascota-form-input'}),
            'pelaje_tipo': forms.TextInput(attrs={'class': 'mascota-form-input'}),
            'caracteristicas_distintivas': forms.Textarea(attrs={'class': 'mascota-form-input'}),
            'tamaño': forms.TextInput(attrs={'class': 'mascota-form-input'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'mascota-form-input'}),
            'nombre_dueno': forms.TextInput(attrs={'class': 'mascota-form-input'}),
            'numero_celular_dueno': forms.TextInput(attrs={'class': 'mascota-form-input'}),
            'email_dueno': forms.EmailInput(attrs={'class': 'mascota-form-input'}),
        }