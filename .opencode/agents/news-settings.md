---
description: "Paso 2: configurar en settings.py el directorio de plantillas (templates/ en la raíz, en DIRS) y las rutas de archivos estáticos y de medios. Si MEDIA_URL/MEDIA_ROOT y el servicio de medios en config/urls.py ya existen, verificarlos en vez de duplicarlos."
mode: subagent
tools:
  write: true
  edit: true
---

# news-settings

## Instrucciones

Configurar `config/settings.py` para la app `news`:

1. **Plantillas (TEMPLATES)**: Agregar `BASE_DIR / "templates"` a `DIRS` en la configuración `TEMPLATES`. Mantener `APP_DIRS: True`.
2. **Archivos estáticos**: Verificar `STATIC_URL`, `STATICFILES_DIRS`, `STATIC_ROOT`. Agregar `BASE_DIR / "static"` a `STATICFILES_DIRS` si no existe.
3. **Archivos de medios**: 
   - Verificar si `MEDIA_URL` y `MEDIA_ROOT` ya están definidos (de labs anteriores). Si NO existen, definirlos:
     - `MEDIA_URL = "media/"`
     - `MEDIA_ROOT = BASE_DIR / "media"`
   - En `config/urls.py`, verificar si ya existe el servicio de medios en desarrollo (`static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`). Si no existe, agregarlo dentro del bloque `if settings.DEBUG:`.

## Reglas

- No duplicar configuraciones existentes
- Código y comentarios en INGLÉS
- Verificar antes de agregar