from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


PROYECTOS = [
    {
        "nombre": "ALQIVO",
        "numero": "01",
        "categoria": "PropTech · Producto digital",
        "descripcion": "Una plataforma para centralizar la operación de alquileres temporarios y convertir tareas dispersas en un proceso trazable.",
        "problema": "Reservas, gastos, propietarios y atención al huésped distribuidos entre planillas y mensajes.",
        "resultado": "Un flujo único para administrar unidades, liquidaciones, equipo operativo y experiencia del huésped.",
        "tecnologias": ["Next.js", "Supabase", "Datos", "UX"],
        "estado": "Producto en evolución",
    },
    {
        "nombre": "Faro Finanzas",
        "numero": "02",
        "categoria": "FinTech · Análisis de datos",
        "descripcion": "Una herramienta personal para entender patrimonio, inversiones y objetivos sin perder la trazabilidad de cada movimiento.",
        "problema": "Información financiera fragmentada entre bancos, brokers, comprobantes y registros históricos.",
        "resultado": "Una lectura unificada de aportes, saldos, rendimiento y evidencia para tomar mejores decisiones.",
        "tecnologias": ["Python", "Análisis de datos", "Automatización", "UX"],
        "estado": "Uso privado · Iteración continua",
    },
    {
        "nombre": "MN8 Portfolio",
        "numero": "03",
        "categoria": "EdTech · Desarrollo web",
        "descripcion": "Este sitio: portfolio, laboratorio técnico y sistema editorial para transformar aprendizajes en contenido útil.",
        "problema": "Proyectos y conocimientos valiosos sin un espacio propio que muestre el proceso y la capacidad técnica.",
        "resultado": "Una aplicación Django con autenticación, perfiles, imágenes, CRUD, permisos por autor y pruebas automatizadas.",
        "tecnologias": ["Python", "Django", "SQLite", "HTML/CSS"],
        "estado": "Entrega final · Coderhouse",
        "url": "https://github.com/mnoero23/mn8-portfolio-django",
        "url_texto": "Explorar el código",
    },
]


def inicio(request):
    """Muestra la portada profesional con contenido destacado."""
    destacados = Post.objects.filter(estado=Post.PUBLICADO)[:3]
    return render(
        request,
        "posts/inicio.html",
        {"destacados": destacados, "proyectos": PROYECTOS},
    )


def lista_posts(request):
    """Lista únicamente las publicaciones visibles del blog."""
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    return render(request, "posts/lista_posts.html", {"posts": posts})


def detalle_post(request, pk):
    """Muestra una publicación individual, incluida su imagen si existe."""
    visibles = Q(estado=Post.PUBLICADO)
    if request.user.is_authenticated:
        visibles |= Q(autor=request.user)
    post = get_object_or_404(Post.objects.filter(visibles), pk=pk)
    return render(request, "posts/detalle_post.html", {"post": post})


@login_required
def crear_post(request):
    """Crea una publicación procesando datos y archivos."""
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        post = form.save(commit=False)
        post.autor = request.user
        post.save()
        messages.success(request, "La publicación se creó correctamente.")
        return redirect("posts:detalle_post", pk=post.pk)
    return render(request, "posts/post_form.html", {"form": form, "modo": "Crear"})


@login_required
def editar_post(request, pk):
    """Actualiza una publicación existente y permite reemplazar su imagen."""
    post = get_object_or_404(Post, pk=pk, autor=request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == "POST" and form.is_valid():
        post = form.save()
        messages.success(request, "La publicación se actualizó correctamente.")
        return redirect("posts:detalle_post", pk=post.pk)
    return render(
        request,
        "posts/post_form.html",
        {"form": form, "modo": "Editar", "post": post},
    )


@login_required
def eliminar_post(request, pk):
    """Elimina una publicación únicamente después de una confirmación POST."""
    post = get_object_or_404(Post, pk=pk, autor=request.user)
    if request.method == "POST":
        post.delete()
        messages.success(request, "La publicación se eliminó correctamente.")
        return redirect("posts:lista_posts")
    return render(request, "posts/post_confirm_delete.html", {"post": post})


def proyectos(request):
    """Presenta una selección de proyectos de Matías y MN8."""
    return render(request, "posts/proyectos.html", {"proyectos": PROYECTOS})


def acerca(request):
    """Presenta al autor y el propósito del proyecto."""
    return render(request, "posts/acerca.html")
