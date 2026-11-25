from django.conf import settings
from django.db import models


class Post(models.Model):
    """Representa una publicación administrable del blog."""

    BORRADOR = "borrador"
    PUBLICADO = "publicado"
    ARCHIVADO = "archivado"
    ESTADOS = [
        (BORRADOR, "Borrador"),
        (PUBLICADO, "Publicado"),
        (ARCHIVADO, "Archivado"),
    ]

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="publicaciones",
        null=True,
        blank=True,
    )
    autor_legacy = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default=BORRADOR)
    imagen = models.ImageField(upload_to="posts/", null=True, blank=True)

    class Meta:
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.titulo

    @property
    def nombre_autor(self):
        """Devuelve el nombre público del usuario o conserva la autoría histórica."""
        if self.autor:
            return self.autor.get_full_name() or self.autor.username
        return self.autor_legacy or "MN8"
