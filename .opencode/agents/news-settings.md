---
description: "Paso 2: configurar en settings.py el directorio de plantillas (templates/ en la raíz, en DIRS) y las rutas de archivos estáticos y de medios. Si MEDIA_URL/MEDIA_ROOT y el servicio de medios en config/urls.py ya existen, verificarlos en vez de duplicarlos."
mode: subagent
tools:
  write: true
  edit: true
---

# news-settings

## Objetivo
Configurar plantillas, estáticos y medios en `config/settings.py` sin duplicar lo ya existente.

## Instrucciones
1. En `config/settings.py`, asegurar que `TEMPLATES[0]['DIRS']` incluya `BASE_DIR / "templates"` (raíz del proyecto). `APP_DIRS` debe quedar en `True`.
2. Verificar `STATIC_URL`, `STATICFILES_DIRS` y `STATIC_ROOT`; agregar `BASE_DIR / "static"` a `STATICFILES_DIRS` si no está.
3. Verificar `MEDIA_URL` y `MEDIA_ROOT`:
   - Si ya existen (configurados en laboratorios anteriores), **no duplicarlos**, solo confirmar que apuntan a `BASE_DIR / "media"`.
   - Si no existen, crearlos: `MEDIA_URL = "/media/"`, `MEDIA_ROOT = BASE_DIR / "media"`.
4. En `config/urls.py`, verificar que el servicio de medios en desarrollo (`static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`) ya esté presente; si no, agregarlo **solo en desarrollo** (`if settings.DEBUG:`).
5. No tocar configuraciones de `library` ni `movies`.

## Reglas
- Código y comentarios en INGLÉS.
- Seguir `docs/news-data-model-spec.md` como única fuente de verdad.
- No romper configuraciones existentes.