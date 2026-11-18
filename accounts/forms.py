from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Perfil


class RegistroForm(UserCreationForm):
    """Registro de usuario con los datos básicos de contacto."""

    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        labels = {
            "username": "Nombre de usuario",
            "first_name": "Nombre",
            "last_name": "Apellido",
        }


class UsuarioForm(forms.ModelForm):
    """Permite mantener actualizados los datos visibles del usuario."""

    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        labels = {"first_name": "Nombre", "last_name": "Apellido"}


class PerfilForm(forms.ModelForm):
    """Edita la presentación profesional y el avatar del perfil."""

    class Meta:
        model = Perfil
        fields = ("biografia", "avatar", "link_web")
        labels = {
            "biografia": "Biografía",
            "avatar": "Avatar",
            "link_web": "Sitio web",
        }
        widgets = {
            "biografia": forms.Textarea(
                attrs={"rows": 6, "placeholder": "Contá brevemente quién sos y qué hacés..."}
            ),
            "link_web": forms.URLInput(attrs={"placeholder": "https://..."}),
        }

