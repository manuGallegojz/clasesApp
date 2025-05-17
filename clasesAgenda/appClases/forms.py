from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    nombre = forms.CharField(
        max_length=40,
        label="Nombre completo",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: Juan Pérez'
        })
    )

    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: juan@mail.com'
        })
    )

    telefono = forms.IntegerField(
        label="Teléfono",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 1123456789'
        })
    )

    username = forms.CharField(
        max_length=40,
        label="Nombre de Usuario",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: manugallego_'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'nombre', 'email', 'telefono' ]