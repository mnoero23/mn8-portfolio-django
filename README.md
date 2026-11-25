# MN8 · Portfolio profesional con Python y Django

Sitio profesional de **Matías Noero** para presentar experiencia, proyectos y artículos sobre gestión, datos y productos digitales. El proyecto consolida la entrega final del curso de Python de Coderhouse y demuestra una aplicación Django completa, segura, documentada y reproducible.

## Propuesta de valor

MN8 combina conocimiento de negocio con capacidad técnica. El sitio presenta proyectos reales —**FARO**, **ALQIVO** y este portfolio— y funciona como sistema editorial para reutilizar aprendizajes en LinkedIn, GitHub y futuras oportunidades profesionales.

## Tecnologías

- Python 3.12+
- Django 5.2.12
- Pillow 12.0.0
- python-decouple 3.8
- SQLite, HTML5 y CSS3
- Git y GitHub

## Funcionalidades

- Portada profesional y portfolio de proyectos.
- Listado público y detalle de artículos publicados.
- CRUD completo de publicaciones desde la interfaz web.
- Imágenes opcionales mediante `ImageField`.
- Registro, login y logout con autenticación de Django.
- Perfil relacionado con `User` mediante `OneToOneField`.
- Edición de nombre, email, biografía, sitio web y avatar.
- Autoría real mediante `ForeignKey(User)`.
- Edición y eliminación limitadas al propietario del artículo.
- Variables sensibles configurables desde `.env`.
- Contenido editorial inicial reproducible mediante migración.
- Diseño responsive, mensajes de éxito y estados seguros sin imagen.
- Panel de administración y 39 pruebas automatizadas.

## Instalación limpia en Windows

### 1. Clonar el repositorio

```powershell
git clone https://github.com/mnoero23/mn8-portfolio-django.git
cd mn8-portfolio-django
```

### 2. Crear y activar el entorno virtual

```powershell
py -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Configurar variables de entorno

```powershell
Copy-Item .env.example .env
```

El archivo `.env.example` documenta las variables necesarias:

```env
SECRET_KEY=reemplazar-por-una-clave-segura
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

`.env` contiene configuración privada y está excluido mediante `.gitignore`. Nunca debe publicarse.

### 5. Aplicar migraciones

```powershell
python manage.py migrate
```

Este paso crea las tablas y carga tres artículos iniciales de MN8. No se necesita `db.sqlite3` para reconstruir el proyecto.

### 6. Crear un administrador

```powershell
python manage.py createsuperuser
```

La contraseña no se muestra mientras se escribe; es el comportamiento normal de la terminal.

### 7. Ejecutar

```powershell
python manage.py runserver
```

Abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Verificación técnica

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test -v 2
```

Resultado esperado:

- `System check identified no issues`.
- `No changes detected`.
- `Ran 39 tests`.
- `OK`.

## Rutas principales

| Ruta | Acceso | Función |
|---|---|---|
| `/` | Público | Portada profesional |
| `/proyectos/` | Público | Casos FARO, ALQIVO y MN8 |
| `/acerca/` | Público | Perfil profesional |
| `/posts/` | Público | Artículos publicados |
| `/posts/<id>/` | Público si está publicado | Detalle del artículo. El borrador es visible para su autor |
| `/posts/crear/` | Autenticado | Crear artículo |
| `/posts/<id>/editar/` | Propietario | Editar artículo |
| `/posts/<id>/eliminar/` | Propietario | Eliminar con confirmación |
| `/cuentas/registro/` | Público | Crear cuenta |
| `/cuentas/login/` | Público | Iniciar sesión |
| `/cuentas/perfil/` | Autenticado | Ver perfil |
| `/cuentas/perfil/editar/` | Autenticado | Editar perfil y avatar |
| `/admin/` | Administrador | Administración de Django |

## Recorrido recomendado para evaluar

1. Abrir la portada, proyectos, artículos y acerca de mí sin iniciar sesión.
2. Registrar un usuario o ingresar con uno existente.
3. Editar el perfil y cargar un avatar.
4. Crear un artículo publicado con imagen.
5. Editarlo y comprobar el mensaje de éxito.
6. Crear otro artículo sin imagen y verificar que no se rompa el diseño.
7. Eliminar una publicación pasando por la confirmación.
8. Cerrar sesión y comprobar que el contenido público continúa visible.
9. Intentar entrar a una ruta protegida y verificar la redirección al login.

## Arquitectura

```text
mn8-portfolio-django/
├── accounts/                 # autenticación y perfiles
├── blog_project/             # configuración general y URLs
├── posts/                    # publicaciones, portfolio y CRUD
│   ├── migrations/           # esquema y contenido reproducible
│   ├── static/posts/css/     # identidad visual MN8
│   └── templates/posts/      # templates con herencia
├── .env.example              # contrato de configuración
├── .gitignore                # exclusiones Python/Django/Windows
├── manage.py
├── PRUEBAS.md
└── requirements.txt
```

## Decisiones técnicas

- Las vistas de creación, edición, eliminación y perfil usan `@login_required`.
- Edición y eliminación buscan el post por `pk` y `request.user`; otro usuario recibe 404.
- `PostForm` no permite elegir autor: la vista asigna al usuario autenticado.
- Las imágenes se procesan con `request.FILES` y `multipart/form-data`.
- `MEDIA_URL` se sirve desde Django solamente en desarrollo con `DEBUG=True`.
- Los artículos iniciales están en una migración de datos, por lo que una base vacía se reconstruye con `migrate`.
- `db.sqlite3`, `media/`, `venv/` y `.env` no se versionan.

## Autor

**Matías Noero** — Licenciado en Administración, analista de datos y creador de productos digitales.

- GitHub: [mnoero23](https://github.com/mnoero23)
- LinkedIn: [matias-noero-samper](https://www.linkedin.com/in/matias-noero-samper/)

Desarrollado como entrega final del curso de Python de Coderhouse y como base profesional de **MN8 · Ideas, datos y productos digitales**.
