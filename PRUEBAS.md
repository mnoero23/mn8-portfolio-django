# Pruebas · MN8 Portfolio Django

## Comandos obligatorios

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test -v 2
```

## Cobertura automatizada

La suite contiene **32 pruebas**: conserva las 20 verificaciones anteriores y suma 12 casos para la Pre-entrega 11.

Se valida:

- Modelo `Perfil` relacionado con `User` mediante `OneToOneField`.
- Formulario personalizado basado en `UserCreationForm`.
- Registro con creación explícita del perfil, sin signals.
- Login con redirección al perfil.
- Logout mediante POST con redirección al listado.
- Protección de la página de perfil.
- Visualización de usuario, email y biografía.
- Edición de datos, biografía, sitio web y avatar.
- Procesamiento del avatar mediante `request.FILES`.
- Protección de crear, editar y borrar posts.
- Acceso público al listado y al detalle de posts.
- Navegación diferenciada para usuarios anónimos y autenticados.
- Regresión completa del CRUD de posts e imágenes.

## Resultado verificado

- `System check identified no issues (0 silenced)`.
- `No changes detected`.
- `Ran 32 tests`.
- `OK`.

## Prueba manual de aceptación

1. Ejecutar `python manage.py migrate` y `python manage.py runserver`.
2. Visitar `/cuentas/registro/` y crear un usuario.
3. Iniciar sesión en `/cuentas/login/`.
4. Confirmar que la navegación muestre **Mi perfil**, **Crear artículo** y **Cerrar sesión**.
5. Abrir el perfil y editar nombre, email, biografía, sitio web y avatar.
6. Confirmar que el avatar se vea y que el perfil muestre la información guardada.
7. Crear, editar y eliminar un artículo estando autenticado.
8. Cerrar sesión.
9. Confirmar que listado y detalle sigan siendo públicos.
10. Escribir directamente las URLs de crear, editar y eliminar y verificar la redirección al login.
11. Revisar la navegación y el perfil en vista móvil.

