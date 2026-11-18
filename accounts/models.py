from django.conf import settings
from django.db import models


class Perfil(models.Model):
    """Información profesional adicional asociada a un usuario de Django."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="perfil",
    )
    biografia = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="perfiles/", null=True, blank=True)
    link_web = models.URLField(blank=True)

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"

    def __str__(self):
        return f"Perfil de {self.user.username}"

