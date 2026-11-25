# Pasos para revisar y presentar la Entrega Final

## 1. Actualizar la rama de revisión

```powershell
# Ejecutar desde la carpeta que contiene manage.py.
git fetch origin
git switch feature/entrega-final-mn8
git pull origin feature/entrega-final-mn8
```

## 2. Preparar y reconstruir

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
if (-not (Test-Path .env)) { Copy-Item .env.example .env }
python manage.py migrate
```

Si el entorno virtual pertenece a otra computadora, renombrarlo y crearlo nuevamente antes de instalar dependencias.

## 3. Validar

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test -v 2
python manage.py runserver
```

Seguir el recorrido manual de `PRUEBAS.md` y revisar escritorio y celular.

## 4. Auditar Git

```powershell
git status
git log --oneline -12
git ls-files | Select-String '(^|/)(venv[^/]*|db\.sqlite3|media|\.env)(/|$)'
git grep -n -F 'C:\Users\'
git diff --check origin/main...HEAD
```

La rama debe estar limpia. Las búsquedas revisan archivos locales y rutas absolutas, y el último comando comprueba el formato del diff.

## 5. Fusionar y presentar

Sólo después de la revisión visual y autorización expresa:

1. Fusionar el PR #4 con `main`.
2. Actualizar la copia local de `main`.
3. Repetir las pruebas finales.
4. Entregar en Coderhouse la URL directa:

`https://github.com/mnoero23/mn8-portfolio-django`
