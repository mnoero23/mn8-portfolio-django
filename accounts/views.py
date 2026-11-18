from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import PerfilForm, RegistroForm, UsuarioForm
from .models import Perfil


def registro(request):
    """Crea el usuario y su perfil explícitamente, sin depender de signals."""
    if request.user.is_authenticated:
        return redirect("accounts:perfil")

    form = RegistroForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        usuario = form.save()
        Perfil.objects.create(user=usuario)
        messages.success(request, "Tu cuenta se creó correctamente. Ya podés iniciar sesión.")
        return redirect("accounts:login")
    return render(request, "accounts/registro.html", {"form": form})


@login_required
def perfil(request):
    """Muestra el perfil privado del usuario autenticado."""
    perfil_usuario, _ = Perfil.objects.get_or_create(user=request.user)
    return render(request, "accounts/perfil.html", {"perfil": perfil_usuario})


@login_required
def editar_perfil(request):
    """Actualiza datos del usuario, biografía, sitio web y avatar."""
    perfil_usuario, _ = Perfil.objects.get_or_create(user=request.user)
    usuario_form = UsuarioForm(request.POST or None, instance=request.user)
    perfil_form = PerfilForm(
        request.POST or None,
        request.FILES or None,
        instance=perfil_usuario,
    )
    if request.method == "POST" and usuario_form.is_valid() and perfil_form.is_valid():
        usuario_form.save()
        perfil_form.save()
        messages.success(request, "Tu perfil se actualizó correctamente.")
        return redirect("accounts:perfil")
    return render(
        request,
        "accounts/editar_perfil.html",
        {"usuario_form": usuario_form, "perfil_form": perfil_form},
    )

