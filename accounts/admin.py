from django.contrib import admin

from .models import Perfil


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("user", "tiene_avatar", "link_web")
    search_fields = ("user__username", "user__email", "biografia")

    @admin.display(boolean=True, description="Avatar")
    def tiene_avatar(self, obj):
        return bool(obj.avatar)

