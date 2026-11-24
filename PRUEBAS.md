# Pruebas · MN8 Portfolio Django

## Comandos obligatorios

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test -v 2
```

## Cobertura automatizada

La suite contiene **38 pruebas** y valida:

- Configuración regional y aplicaciones instaladas.
- Portada, navegación, portfolio y archivos estáticos.
- Contenido editorial reproducible mediante migración.
- Modelo `Post`, estados y orden descendente.
- Listado público y detalle de publicaciones.
- CRUD con mensajes de éxito y confirmación de borrado.
- Imagen opcional, Pillow, `request.FILES` y formulario multipart.
- Registro basado en `UserCreationForm`.
- Perfil `OneToOneField`, biografía, web y avatar.
- Login, logout por POST y rutas protegidas.
- Autoría automática mediante el usuario autenticado.
- Edición y eliminación permitidas solamente al propietario.
- Navegación diferenciada para visitantes y usuarios autenticados.

## Resultado esperado

- `System check identified no issues (0 silenced)`.
- `No changes detected`.
- `Ran 38 tests`.
- `OK`.

## Prueba manual de aceptación

1. Ejecutar migraciones y levantar el servidor.
2. Como visitante, recorrer `/`, `/proyectos/`, `/acerca/` y `/posts/`.
3. Confirmar que aparezcan los tres artículos iniciales de MN8.
4. Registrar un usuario e iniciar sesión.
5. Editar nombre, email, biografía, sitio web y avatar.
6. Crear un artículo publicado con imagen.
7. Editarlo y verificar la confirmación visual.
8. Crear un artículo sin imagen.
9. Eliminar una publicación pasando por la pantalla de confirmación.
10. Cerrar sesión y confirmar que listado y detalle sigan siendo públicos.
11. Intentar abrir crear, editar, eliminar y perfil sin sesión.
12. Comprobar que otro usuario no pueda editar ni borrar publicaciones ajenas.
13. Revisar portada, login, perfil, artículos y proyectos en ancho móvil.

## Reconstrucción limpia

En una copia nueva del repositorio:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py test -v 2
python manage.py runserver
```

La aplicación debe iniciar sin depender de `db.sqlite3`, `media/` ni configuraciones de otra computadora.
