---
description: "Create movies app structure, install Pillow, add to INSTALLED_APPS"
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# movies-project-structure

## Objetivo
Paso 1: Crear la app `movies`, instalar Pillow (si no está ya), declarar `movies` en `INSTALLED_APPS` junto a `library`.

## Instrucciones

### 1. Verificar estado actual
- Leer `config/settings.py` para ver cómo está configurada `library` en `INSTALLED_APPS`.
- Verificar si `Pillow` ya está en `requirements.txt` o `pyproject.toml`.

### 2. Crear la app movies
```bash
python manage.py startapp movies
```

### 3. Instalar Pillow
```bash
pip install Pillow
# Actualizar requirements.txt
pip freeze > requirements.txt
```

### 4. Registrar en INSTALLED_APPS
En `config/settings.py`, añadir `'movies'` en `INSTALLED_APPS` **después** de `'library'` (mantener el mismo patrón):
```python
INSTALLED_APPS = [
    ...
    'library',
    'movies',
    ...
]
```

### 5. Verificar estructura
Comprobar que `movies/` tiene:
- `models.py`
- `admin.py`
- `apps.py`
- `views.py`
- `migrations/`
- `tests.py`

### 6. Configurar MEDIA_URL/MEDIA_ROOT (si no existe)
En `config/settings.py`, si no están definidos:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### 7. Servir media en desarrollo
En `config/urls.py`, añadir (solo si no existe ya):
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... tus urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Reglas obligatorias
- **No modificar** la app `library` ni su configuración.
- Código y comentarios en **INGLÉS**. Explicaciones al usuario en **ESPAÑOL**.
- Seguir exactamente `docs/movies-data-model-spec.md` como única fuente de verdad.
- Antes de tocar `config/settings.py` o `config/urls.py`, revisar cómo está `library` y seguir el mismo patrón.
- Ante duda sobre conceptos no vistos en clase, **preguntar al usuario**.