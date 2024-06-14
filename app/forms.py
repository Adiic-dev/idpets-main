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
    
from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'mascota-form-input', 'id': 'id_nombre'}),
            'especie': forms.Select(attrs={'class': 'mascota-form-input', 'id': 'id_especie'}),
            'raza': forms.TextInput(attrs={'class': 'mascota-form-input', 'id': 'id_raza'}),
            'sexo': forms.Select(attrs={'class': 'mascota-form-input', 'id': 'id_sexo'}),
            'edad': forms.NumberInput(attrs={'class': 'mascota-form-input', 'id': 'id_edad'}),
            'pelaje_color': forms.TextInput(attrs={'class': 'mascota-form-input', 'id': 'id_pelaje_color'}),
            'pelaje_tipo': forms.Select(attrs={'class': 'mascota-form-input', 'id': 'id_pelaje_tipo'}),
            'caracteristicas_distintivas': forms.Textarea(attrs={'class': 'mascota-form-input', 'id': 'id_caracteristicas_distintivas'}),
            'tamaño': forms.Select(attrs={'class': 'mascota-form-input', 'id': 'id_tamaño'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'mascota-form-input', 'id': 'id_foto'}),
            'nombre_dueno': forms.TextInput(attrs={'class': 'mascota-form-input', 'id': 'id_nombre_dueno'}),
            'numero_celular_dueno': forms.TextInput(attrs={'class': 'mascota-form-input', 'id': 'id_numero_celular_dueno'}),
            'email_dueno': forms.EmailInput(attrs={'class': 'mascota-form-input', 'id': 'id_email_dueno'}),
        }
