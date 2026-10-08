---
description: "Paso 3: declarar Author, Category y Article según el spec, con Meta y __str__. Justificar cada relación antes de escribirla. Generar y aplicar migraciones, y confirmar que el superusuario existente sigue funcionando (reutilizarlo, no crear otro)."
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# news-models

## Objetivo
Declarar los modelos `Author`, `Category` y `Article` en `news/models.py` según la especificación.

## Instrucciones
1. En `news/models.py`, crear las tres clases con sus campos, `Meta` y `__str__` exactamente como dice `docs/news-data-model-spec.md`.
2. **Justificar cada relación** en comentarios antes de escribirla:
   - `Article.author`: ForeignKey a `Author`, `on_delete=PROTECT`, `related_name="articles"` → *Borrar un autor no debe arrastrar sus noticias publicadas.*
   - `Article.categories`: ManyToManyField a `Category`, `related_name="articles"` → *Una noticia puede tener varias categorías y una categoría varias noticias.*
3. Importar `timezone` de `django.utils` para el `default` de `published_at`.
4. Generar migraciones: `python manage.py makemigrations news`.
5. Aplicar migraciones: `python manage.py migrate`.
6. Verificar que el superusuario existente sigue funcionando: `python manage.py shell -c "from django.contrib.auth import get_user_model; print(get_user_model().objects.filter(is_superuser=True).exists())"`.
   - **No crear otro superusuario**, reutilizar el que ya existe.

## Reglas
- Código y comentarios en INGLÉS.
- Nombres de modelos en singular, campos exactamente como en el spec.
- No modificar `library` ni `models` de otras apps.
- Seguir `docs/news-data-model-spec.md` como única fuente de verdad.