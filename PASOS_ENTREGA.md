# Pasos para revisar y presentar la Entrega Final

## 1. Actualizar la rama de revisión

```powershell
cd "$env:USERPROFILE\OneDrive\PERSONAL\01. CURSOS\02 - CODERHOUSE\2026 - Python\Modulo 6 - Git GitHub e introduccion a Django\07 - Preentrega 7"
git fetch origin
git switch feature/entrega-final-mn8
git pull origin feature/entrega-final-mn8
```

## 2. Preparar y reconstruir

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env -ErrorAction SilentlyContinue
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
git ls-files | Select-String "(^|/)(venv|db.sqlite3|media|\.env)$"
git grep -n "C:\\Users\\"
```

El árbol debe estar limpio y las dos búsquedas finales no deben encontrar archivos privados ni rutas absolutas.

## 5. Fusionar y presentar

Sólo después de la revisión visual y autorización expresa:

1. Fusionar el PR #4 con `main`.
2. Actualizar la copia local de `main`.
3. Repetir las pruebas finales.
4. Entregar en Coderhouse la URL directa:

`https://github.com/mnoero23/mn8-portfolio-django`
