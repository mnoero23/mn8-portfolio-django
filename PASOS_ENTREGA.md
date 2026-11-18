# Pasos para revisar y entregar la Pre-entrega 11

## 1. Actualizar la copia local

```powershell
cd "$env:USERPROFILE\OneDrive\PERSONAL\01. CURSOS\02 - CODERHOUSE\2026 - Python\Modulo 6 - Git GitHub e introduccion a Django\07 - Preentrega 7"
git fetch origin
git switch feature/preentrega-11-autenticacion
git pull origin feature/preentrega-11-autenticacion
```

## 2. Preparar el entorno

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
```

Si el entorno virtual fue creado en otra computadora o con otra instalación de Python, recrearlo:

```powershell
deactivate
Rename-Item venv venv_anterior
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
```

## 3. Verificar

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test -v 2
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/` y seguir la prueba manual de `PRUEBAS.md`.

## 4. Confirmar la rama

```powershell
git status
git log --oneline -6
```

## 5. Entregar

Después de aprobar la revisión visual y fusionar el PR con autorización expresa, pegar en Coderhouse:

`https://github.com/mnoero23/mn8-portfolio-django`

