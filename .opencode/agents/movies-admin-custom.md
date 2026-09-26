---
description: "Replace simple registration with ModelAdmin classes, list_display, filters, search, inlines, readonly_fields"
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# movies-admin-custom

## Objetivo
Pasos 5-7: Reemplazar el registro simple por clases `ModelAdmin`. Definir `list_display` con columnas útiles, `list_filter` por género y año, `search_fields` por título y nombre de persona. Añadir `Rating` como `TabularInline` dentro de `MovieAdmin`. Marcar `created_at` y `updated_at` como `readonly_fields` y comprobar que el panel ya no permite editarlos.

## Instrucciones

### 1. Reescribir movies/admin.py completo
```python
from django.contrib import admin
from .models import Genre, Person, Movie, Rating


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1
    readonly_fields = ("created_at",)
    fields = ("score", "comment", "created_at")
    ordering = ("-created_at",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "movie_count")
    search_fields = ("name",)
    ordering = ("name",)

    @admin.display(description="Movies")
    def movie_count(self, obj):
        return obj.movies.count()


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("full_name", "role", "photo_preview")
    list_filter = ("role",)
    search_fields = ("first_name", "last_name")
    ordering = ("last_name", "first_name")
    readonly_fields = ("photo_preview",)

    @admin.display(description="Name")
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    @admin.display(description="Photo")
    def photo_preview(self, obj):
        if obj.photo:
            from django.utils.html import format_html
            return format_html('<img src="{}" width="50" />', obj.photo.url)
        return "—"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "release_year", "genre_list", "avg_rating", "created_at")
    list_filter = ("genres", "release_year")
    search_fields = ("title", "synopsis")
    ordering = ("-release_year", "title")
    readonly_fields = ("created_at", "updated_at")
    filter_horizontal = ("genres",)
    inlines = (RatingInline,)

    @admin.display(description="Genres")
    def genre_list(self, obj):
        return ", ".join(g.name for g in obj.genres.all())

    @admin.display(description="Avg Rating")
    def avg_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings:
            avg = sum(r.score for r in ratings) / len(ratings)
            return f"{avg:.1f}/10"
        return "—"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("movie", "score", "comment_short", "created_at")
    list_filter = ("score", "created_at")
    search_fields = ("movie__title", "comment")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    @admin.display(description="Comment")
    def comment_short(self, obj):
        return obj.comment[:50] + "..." if len(obj.comment) > 50 else obj.comment
```

### 2. Verificar en Django Admin
- Recargar `http://127.0.0.1:8000/admin/`.
- Comprobar cada modelo:

**GenreAdmin**:
- Lista muestra `name` y `movie_count`.
- Buscar por nombre funciona.

**PersonAdmin**:
- Lista muestra `full_name`, `role`, `photo_preview` (miniatura).
- Filtro por `role` (director/actor).
- Buscar por first_name/last_name.
- `photo_preview` es readonly.

**MovieAdmin**:
- Lista: `title`, `release_year`, `genre_list`, `avg_rating`, `created_at`.
- Filtros laterales: `genres` (checkbox), `release_year` (dropdown).
- Buscar por `title`, `synopsis`.
- `filter_horizontal` para géneros (widget M2M amigable).
- **Inline**: `RatingInline` aparece abajo → añadir/editar ratings sin salir.
- `created_at`, `updated_at` en `readonly_fields` → **no editables** en formulario.

**RatingAdmin**:
- Lista: `movie`, `score`, `comment_short`, `created_at`.
- Filtros: `score`, `created_at`.
- Buscar por `movie__title`, `comment`.
- `created_at` readonly.

### 3. Probar readonly_fields
- Editar una `Movie` → confirmar que `created_at` y `updated_at` **no tienen input**, solo texto.
- Editar un `Rating` → `created_at` no editable.
- Intentar cambiar vía POST (opcional): confirmar que Django ignora cambios en readonly.

### 4. Verificar inline
- En edición de `Movie`: añadir 2-3 ratings inline → "Save" → verificar que se guardan.
- Borrar inline → "Save" → verificar borrado.

## Reglas obligatorias
- **No modificar** `library/admin.py`.
- Código y comentarios en **INGLÉS**. Explicaciones al usuario en **ESPAÑOL**.
- Usar `@admin.register` decorator (estilo moderno).
- `list_display` con métodos `@admin.display` para columnas calculadas.
- `readonly_fields` exactos: `created_at`, `updated_at` (Movie), `created_at` (Rating), `photo_preview` (Person).
- `filter_horizontal` para M2M `genres`.
- `TabularInline` para `Rating` (no `StackedInline`).
- Ante duda, **preguntar al usuario**.