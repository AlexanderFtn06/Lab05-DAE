---
description: "Paso 11: personalizar el administrador de Author, Category y Article con list_display, list_filter y search_fields (y prepopulated_fields para los slug). Dar de alta, desde el panel, las seis noticias en tres categorías definidas en el spec, y comprobar que aparecen en el portal."
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# news-admin

## Instrucciones

Personalizar `news/admin.py`:

### AuthorAdmin
- `list_display = ["first_name", "last_name", "photo_preview"]`
- `search_fields = ["first_name", "last_name"]`
- `list_filter = []`
- Método `photo_preview`: miniatura de la foto (50px) o "Sin foto"

### CategoryAdmin
- `list_display = ["name", "slug", "articles_count"]`
- `prepopulated_fields = {"slug": ("name",)}`
- `search_fields = ["name"]`
- `list_filter = []`
- Método `articles_count`: `return obj.articles.count()`

### ArticleAdmin
- `list_display = ["title", "author", "published_at", "categories_display", "featured_image_preview"]`
- `list_filter = ["categories", "published_at", "author"]`
- `search_fields = ["title", "summary", "body"]`
- `prepopulated_fields = {"slug": ("title",)}`
- `date_hierarchy = "published_at"`
- `raw_id_fields = ["author"]` (opcional)
- Métodos:
  - `categories_display`: ", ".join([c.name for c in obj.categories.all()])
  - `featured_image_preview`: miniatura 50px o "Sin imagen"

### Registrar
```python
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
```

### Cargar datos de prueba (via admin panel)
1. **3 Categorías**: Tecnología, Deportes, Cultura
2. **2 Autores**: con nombre, apellido, bio, foto opcional
3. **6 Noticias** (2 por categoría), al menos 1 en 2 categorías:
   - Verificar en portal: `/news/`, `/news/category/<slug>/`, `/news/article/<slug>/`

## Reglas

- `prepopulated_fields` para slugs
- Código y comentarios en INGLÉS
- Reutilizar superusuario existente (NO crear otro)
- Verificar que se ven en el portal