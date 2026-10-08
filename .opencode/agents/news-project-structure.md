---
description: "Paso 1: crear la app news, instalar Pillow si no está ya, y declarar news en INSTALLED_APPS después de library y movies."
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# news-project-structure

## Objetivo
Crear la estructura inicial de la app `news` siguiendo el patrón del proyecto existente.

## Instrucciones
1. Verificar que `Pillow` está instalado (`pip show Pillow`); si no, instalarlo (`pip install Pillow`).
2. Crear la app: `python manage.py startapp news`.
3. En `config/settings.py`, agregar `'news'` a `INSTALLED_APPS` **después de** `'library'` y `'movies'`.
4. Verificar que la estructura de directorios sea correcta:
   ```
   news/
   ├── __init__.py
   ├── admin.py
   ├── apps.py
   ├── migrations/
   ├── models.py
   ├── tests.py
   ├── views.py
   └── ...
   ```
5. No modificar `library` ni `movies` en ningún momento.

## Reglas
- Código y comentarios en INGLÉS.
- Seguir `docs/news-data-model-spec.md` como única fuente de verdad.