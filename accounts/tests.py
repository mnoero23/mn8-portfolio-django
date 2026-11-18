import base64
import shutil
import tempfile

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from posts.models import Post

from .forms import RegistroForm
from .models import Perfil


MEDIA_TEMPORAL = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_TEMPORAL)
class AutenticacionYPerfilTest(TestCase):
    """Valida los requisitos funcionales de la Pre-entrega 11."""

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(MEDIA_TEMPORAL, ignore_errors=True)

    def setUp(self):
        self.usuario = User.objects.create_user(
            username="matu",
            email="matu@example.com",
            password="ClaveSegura123!",
            first_name="Matías",
            last_name="Noero",
        )
        self.perfil = Perfil.objects.create(
            user=self.usuario,
            biografia="Analista de datos y creador de productos digitales.",
        )
        self.post = Post.objects.create(
            titulo="Artículo público",
            contenido="Contenido visible para visitantes.",
            autor="Matías Noero",
            estado=Post.PUBLICADO,
        )

    def test_perfil_usa_relacion_uno_a_uno(self):
        campo = Perfil._meta.get_field("user")
        self.assertTrue(campo.one_to_one)
        self.assertEqual(self.usuario.perfil, self.perfil)

    def test_formulario_de_registro_se_basa_en_user_creation_form(self):
        self.assertTrue(issubclass(RegistroForm, __import__(
            "django.contrib.auth.forms",
            fromlist=["UserCreationForm"],
        ).UserCreationForm))

    def test_registro_crea_usuario_y_perfil_sin_signals(self):
        respuesta = self.client.post(
            reverse("accounts:registro"),
            {
                "username": "nuevo",
                "first_name": "Nuevo",
                "last_name": "Usuario",
                "email": "nuevo@example.com",
                "password1": "ClaveMuySegura456!",
                "password2": "ClaveMuySegura456!",
            },
        )
        usuario = User.objects.get(username="nuevo")
        self.assertRedirects(respuesta, reverse("accounts:login"))
        self.assertTrue(Perfil.objects.filter(user=usuario).exists())

    def test_login_redirige_al_perfil(self):
        respuesta = self.client.post(
            reverse("accounts:login"),
            {"username": "matu", "password": "ClaveSegura123!"},
        )
        self.assertRedirects(respuesta, reverse("accounts:perfil"))

    def test_logout_por_post_redirige_al_listado(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.post(reverse("accounts:logout"))
        self.assertRedirects(respuesta, reverse("posts:lista_posts"))
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_perfil_requiere_autenticacion(self):
        respuesta = self.client.get(reverse("accounts:perfil"))
        destino = f"{reverse('accounts:login')}?next={reverse('accounts:perfil')}"
        self.assertRedirects(respuesta, destino)

    def test_perfil_muestra_datos_del_usuario(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.get(reverse("accounts:perfil"))
        self.assertContains(respuesta, "Matías Noero")
        self.assertContains(respuesta, self.usuario.email)
        self.assertContains(respuesta, self.perfil.biografia)

    def test_edicion_procesa_biografia_y_avatar(self):
        png = base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
        )
        avatar = SimpleUploadedFile("avatar.png", png, content_type="image/png")
        self.client.force_login(self.usuario)
        respuesta = self.client.post(
            reverse("accounts:editar_perfil"),
            {
                "first_name": "Matías",
                "last_name": "Noero",
                "email": "matias@example.com",
                "biografia": "Nueva biografía profesional.",
                "link_web": "https://example.com",
                "avatar": avatar,
            },
        )
        self.perfil.refresh_from_db()
        self.assertRedirects(respuesta, reverse("accounts:perfil"))
        self.assertEqual(self.perfil.biografia, "Nueva biografía profesional.")
        self.assertTrue(self.perfil.avatar.name.startswith("perfiles/"))

    def test_crear_editar_y_borrar_posts_requiere_login(self):
        rutas = (
            reverse("posts:crear_post"),
            reverse("posts:editar_post", args=[self.post.pk]),
            reverse("posts:eliminar_post", args=[self.post.pk]),
        )
        for ruta in rutas:
            with self.subTest(ruta=ruta):
                respuesta = self.client.get(ruta)
                self.assertEqual(respuesta.status_code, 302)
                self.assertTrue(respuesta.url.startswith(reverse("accounts:login")))

    def test_listado_y_detalle_siguen_siendo_publicos(self):
        self.assertEqual(self.client.get(reverse("posts:lista_posts")).status_code, 200)
        self.assertEqual(
            self.client.get(reverse("posts:detalle_post", args=[self.post.pk])).status_code,
            200,
        )

    def test_navegacion_anonima_muestra_login_y_registro(self):
        respuesta = self.client.get(reverse("posts:inicio"))
        self.assertContains(respuesta, reverse("accounts:login"))
        self.assertContains(respuesta, reverse("accounts:registro"))
        self.assertNotContains(respuesta, reverse("accounts:perfil"))

    def test_navegacion_autenticada_muestra_perfil_creacion_y_logout(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.get(reverse("posts:inicio"))
        self.assertContains(respuesta, reverse("accounts:perfil"))
        self.assertContains(respuesta, reverse("posts:crear_post"))
        self.assertContains(respuesta, reverse("accounts:logout"))
