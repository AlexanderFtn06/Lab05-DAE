---
description: "Paso 11: personalizar el administrador de Author, Category y Article con list_display, list_filter y search_fields (y prepopulated_fields para los slug). Dar de alta, desde el panel, las seis noticias en tres categorías definidas en el spec, y comprobar que aparecen en el portal."
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# news-admin

## Objetivo
Personalizar el admin de Django para `Author`, `Category` y `Article`, y cargar los datos de prueba.

## Instrucciones
1. En `news/admin.py`, registrar los tres modelos con `ModelAdmin` personalizado:

   **AuthorAdmin**:
   - `list_display = ["first_name", "last_name", "photo_preview"]` (método para miniatura).
   - `search_fields = ["first_name", "last_name"]`.
   - `list_filter = []` (opcional).

   **CategoryAdmin**:
   - `list_display = ["name", "slug", "article_count"]` (método `article_count`).
   - `prepopulated_fields = {"slug": ("name",)}`.
   - `search_fields = ["name"]`.
   - `list_filter = []`.

   **ArticleAdmin**:
   - `list_display = ["title", "author", "published_at", "category_list", "featured_image_preview"]`.
   - `list_filter = ["categories", "published_at", "author"]`.
   - `search_fields = ["title", "summary", "body"]`.
   - `prepopulated_fields = {"slug": ("title",)}`.
   - `date_hierarchy = "published_at"`.
   - `raw_id_fields = ["author"]` (opcional, para rendimiento).
   - Métodos helper: `category_list` (join de nombres), `featured_image_preview` (miniatura).

2. Registrar: `admin.site.register(Author, AuthorAdmin)`, etc.

3. Ejecutar servidor: `python manage.py runserver`, entrar a `/admin/` con el superusuario **existente** (no crear otro).

4. Crear en el admin:
   - 3 categorías: **Tecnología**, **Deportes**, **Cultura** (slugs auto).
   - 2 autores (nombre, apellido, bio, foto opcional).
   - 6 noticias (2 por categoría), al menos **una noticia en dos categorías** (ej. una noticia en Tecnología y Cultura).
   - Completar: título, slug (auto), resumen, cuerpo, imagen destacada (opcional), fecha, autor, categorías.

5. Verificar en el portal (`/news/`, `/news/category/tecnologia/`, `/news/article/<slug>/`) que se ven correctamente.

## Reglas
- Código y comentarios en INGLÉS.
- Usar `prepopulated_fields` para slugs.
- No modificar admin de `library` ni `movies`.
- Seguir `docs/news-data-model-spec.md` como única fuente de verdad.