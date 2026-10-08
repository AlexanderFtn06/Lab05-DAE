---
description: "Paso 1: crear la app news, instalar Pillow si no está ya, y declarar news en INSTALLED_APPS después de library y movies."
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# news-project-structure

## Instrucciones

Crear la estructura inicial del proyecto para la app `news`:

1. Verificar si `Pillow` está instalado (`pip show Pillow`). Si no, instalarlo: `pip install Pillow`
2. Crear la app Django: `python manage.py startapp news`
3. En `config/settings.py`, agregar `'news'` a `INSTALLED_APPS` **después** de `'library'` y `'movies'`
4. Verificar que la estructura de carpetas sea correcta:
   - `news/models.py`
   - `news/views.py`
   - `news/urls.py` (crear si no existe)
   - `news/admin.py`
   - `news/apps.py`
   - `news/migrations/`
   - `news/templates/news/` (crear)
   - `news/static/news/` (crear)

## Reglas

- No modificar `library` ni `movies`
- Seguir la estructura estándar de Django
- Código y comentarios en INGLÉS