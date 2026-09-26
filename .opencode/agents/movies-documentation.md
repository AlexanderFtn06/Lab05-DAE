---
description: "Record admin screenshots before/after customization, superuser vs editor comparison"
mode: subagent
tools:
  read: true
  write: true
---

# movies-documentation

## Objetivo
Paso 11: Registrar en el entregable las capturas del panel antes y después de la personalización, y la comparación de lo que ve el superusuario frente al usuario editor, con el mismo formato que ya se usó en el laboratorio anterior (nombre del alumno, título del desarrollo, captura, código, explicación, casos de prueba).

## Instrucciones

### 1. Formato de documentación (igual que Lab 4)
Crear archivo `docs/lab05-admin-documentation.md` con esta estructura:

```markdown
# Lab 5 - Django Admin (Movies App) - Documentation

**Student:** [Tu Nombre]
**Date:** [Fecha]
**Project:** Lab04-DAE (continuación) → Movies App

---

## 1. Admin Panel - Before Customization (Basic Registration)

### 1.1 Genre Admin
**Screenshot:** `docs/screenshots/admin-basic-genre.png`
**Code:** `movies/admin.py` (versión inicial con `admin.site.register`)
**Explanation:** Registro simple. Solo muestra `__str__` (name). Sin búsqueda, filtros ni columnas extra.
**Test Cases:**
- Create genre "Action" → OK
- List shows name only → OK
- Edit/Delete → OK

### 1.2 Person Admin
**Screenshot:** `docs/screenshots/admin-basic-person.png`
**Code:** `movies/admin.py` (versión inicial)
**Explanation:** Registro simple. Muestra `first_name last_name`. Sin filtro por role ni preview de foto.
**Test Cases:**
- Create person with/without photo → OK
- List shows name only → OK

### 1.3 Movie Admin
**Screenshot:** `docs/screenshots/admin-basic-movie.png`
**Code:** `movies/admin.py` (versión inicial)
**Explanation:** Registro simple. M2M genres como widget básico. Sin inline ratings. Sin columnas calculadas.
**Test Cases:**
- Create movie with genres → OK
- List shows title (year) only → OK

### 1.4 Rating Admin
**Screenshot:** `docs/screenshots/admin-basic-rating.png`
**Code:** `movies/admin.py` (versión inicial)
**Explanation:** Registro simple. FK movie como dropdown. Sin filtro por score.
**Test Cases:**
- Create rating 1-10 → OK
- Cascade delete verified → OK

---

## 2. Admin Panel - After Customization (ModelAdmin Classes)

### 2.1 GenreAdmin
**Screenshot:** `docs/screenshots/admin-custom-genre.png`
**Code:** `movies/admin.py` (clase `GenreAdmin`)
**Explanation:** 
- `list_display = ("name", "movie_count")` → columna calculada con `@admin.display`.
- `search_fields = ("name",)` → búsqueda por nombre.
- `ordering = ("name",)` → orden alfabético.
**Test Cases:**
- Search "Action" → filtra correctamente.
- movie_count muestra número de películas → OK.

### 2.2 PersonAdmin
**Screenshot:** `docs/screenshots/admin-custom-person.png`
**Code:** `movies/admin.py` (clase `PersonAdmin`)
**Explanation:**
- `list_display = ("full_name", "role", "photo_preview")` → métodos personalizados.
- `list_filter = ("role",)` → filtro lateral Director/Actor.
- `search_fields = ("first_name", "last_name")` → búsqueda por nombre/apellido.
- `readonly_fields = ("photo_preview",)` → miniatura no editable.
**Test Cases:**
- Filter by "director" → muestra solo directores.
- Photo preview shows thumbnail → OK.
- Search "Nolan" → encuentra Christopher Nolan.

### 2.3 MovieAdmin
**Screenshot:** `docs/screenshots/admin-custom-movie.png`
**Code:** `movies/admin.py` (clase `MovieAdmin`)
**Explanation:**
- `list_display = ("title", "release_year", "genre_list", "avg_rating", "created_at")` → columnas ricas.
- `list_filter = ("genres", "release_year")` → filtros M2M + año.
- `search_fields = ("title", "synopsis")` → búsqueda full-text básica.
- `filter_horizontal = ("genres",)` → widget M2M usables.
- `readonly_fields = ("created_at", "updated_at")` → timestamps no editables.
- `inlines = (RatingInline,)` → ratings inline (TabularInline).
**Test Cases:**
- Filter by genre "Science Fiction" + year "2014" → Interstellar, etc.
- Inline: add 2 ratings → save → aparecen en lista.
- created_at/updated_at readonly → no inputs, solo texto.
- genre_list muestra "Action, Science Fiction" → OK.
- avg_rating calculado dinámicamente → OK.

### 2.4 RatingAdmin
**Screenshot:** `docs/screenshots/admin-custom-rating.png`
**Code:** `movies/admin.py` (clase `RatingAdmin`)
**Explanation:**
- `list_display = ("movie", "score", "comment_short", "created_at")`.
- `list_filter = ("score", "created_at")`.
- `search_fields = ("movie__title", "comment")` → lookup cross-FK.
- `readonly_fields = ("created_at",)`.
**Test Cases:**
- Filter score=10 → solo 10s.
- Search "Inception" → ratings de Inception.
- comment_short trunca a 50 chars → OK.

### 2.5 RatingInline (en MovieAdmin)
**Screenshot:** `docs/screenshots/admin-custom-movie-inline.png`
**Code:** `movies/admin.py` (clase `RatingInline`)
**Explanation:** `TabularInline` compacto. `extra=1`. `readonly_fields=("created_at",)`.
**Test Cases:**
- Add inline rating → save → persiste.
- Delete inline checkbox → save → borra.
- created_at readonly en inline → OK.

---

## 3. Permissions Comparison: Superuser vs Editor

### 3.1 Setup
**Screenshot:** `docs/screenshots/permissions-group-editors.png`
**Code:** Django Admin → Groups → editors
**Explanation:** Grupo "editors" con perms: add/change/view (Movie, Genre, Person, Rating). SIN delete_*.

### 3.2 Superuser View
**Screenshot:** `docs/screenshots/admin-superuser-movie-list.png`
**Description:** Lista Movies con actions: "Delete selected", botón "Delete" en detalle, inline ratings con checkbox delete.

### 3.3 Editor View
**Screenshot:** `docs/screenshots/admin-editor-movie-list.png`
**Description:** Lista Movies SIN action "Delete selected". Detalle SIN botón "Delete". Inline ratings SIN checkbox delete.

### 3.4 Comparison Table

| Feature | Superuser | Editor (group: editors) |
|---------|-----------|-------------------------|
| View Movies | ✅ | ✅ |
| Add Movie | ✅ | ✅ |
| Change Movie | ✅ | ✅ |
| **Delete Movie** | ✅ | ❌ |
| View/Genre | ✅ | ✅ |
| Add/Change Genre | ✅ | ✅ |
| **Delete Genre** | ✅ | ❌ |
| View/Person | ✅ | ✅ |
| Add/Change Person | ✅ | ✅ |
| **Delete Person** | ✅ | ❌ |
| View/Rating | ✅ | ✅ |
| Add/Change Rating | ✅ | ✅ |
| **Delete Rating** | ✅ | ❌ |
| Inline Rating Delete | ✅ | ❌ |
| Access Auth (Users/Groups) | ✅ | ❌ |

**Test Cases Documentados:**
1. Login editor → crear película → OK.
2. Login editor → editar película → OK.
3. Login editor → intentar borrar película → **no hay opción**.
4. Login editor → añadir rating inline → OK.
5. Login editor → intentar borrar rating inline → **no hay checkbox delete**.
6. Login superusuario → todas las opciones presentes → OK.

---

## 4. Public Recommendation View

### 4.1 All Movies View
**Screenshot:** `docs/screenshots/view-recommendations-all.png`
**URL:** `/movies/`
**Code:** `movies/views.py` (`movie_recommendations`), `movies/templates/movies/recommendations.html`, `movies/static/movies/style.css`
**Explanation:** Vista pública sin login. Grid responsive tarjetas. Orden por avg_rating desc. Fondo #121212, acentos #d4af37/#b8323f.
**Test Cases:**
- Load `/movies/` → 10 películas ordenadas por rating.
- Cards show: poster, title, year, genres, stars + rating value.
- Hover card → lift + gold border.
- Responsive: mobile 1 col, tablet 2+, desktop 4+.

### 4.2 Genre Filtered View
**Screenshot:** `docs/screenshots/view-recommendations-genre.png`
**URL:** `/movies/genre/science-fiction/`
**Explanation:** Filtro por género via URL. Badge muestra género actual. Nav pills para cambiar género.
**Test Cases:**
- Nav click "Science Fiction" → URL cambia, lista filtrada.
- Badge "Science Fiction" visible.
- Only Sci-Fi movies shown.

### 4.3 CSS Theme Verification
**Screenshot:** `docs/screenshots/view-css-variables.png` (DevTools)
**Code:** `movies/static/movies/style.css`
**Explanation:** Variables CSS definidas. Sin frameworks externos. Solo archivo propio.
**Test Cases:**
- Inspect → :root variables match spec.
- No external CSS requests in Network tab.
- Dark mode only (no light mode toggle required).

---

## 5. Test Cases Summary

| # | Description | Expected | Status |
|---|-------------|----------|--------|
| 1 | Basic admin CRUD Genre | Create/Read/Update/Delete | ✅ |
| 2 | Basic admin CRUD Person | Create/Read/Update/Delete | ✅ |
| 3 | Basic admin CRUD Movie | Create/Read/Update/Delete | ✅ |
| 4 | Basic admin CRUD Rating | Create/Read/Update/Delete | ✅ |
| 5 | Cascade delete Movie → Ratings | Ratings deleted | ✅ |
| 6 | Custom GenreAdmin list_display | name, movie_count | ✅ |
| 7 | Custom PersonAdmin photo_preview | Thumbnail visible | ✅ |
| 8 | Custom MovieAdmin inline ratings | Add/edit/delete inline | ✅ |
| 9 | MovieAdmin readonly timestamps | No editable inputs | ✅ |
| 10 | Editor group permissions | add/change only, no delete | ✅ |
| 11 | Editor login verification | Delete options hidden | ✅ |
| 12 | Public view /movies/ | Grid loads, sorted by rating | ✅ |
| 13 | Public view /movies/genre/x/ | Filtered correctly | ✅ |
| 14 | Dark theme CSS applied | Colors match spec | ✅ |
| 15 | Responsive design | Mobile/tablet/desktop OK | ✅ |

---

## 6. Files Modified/Created (Checklist)

- [ ] `movies/models.py` — 4 models per spec
- [ ] `movies/admin.py` — ModelAdmin classes + inline
- [ ] `movies/views.py` — recommendation view
- [ ] `movies/urls.py` — app URLs
- [ ] `movies/templates/movies/recommendations.html` — template
- [ ] `movies/static/movies/style.css` — dark cinema theme
- [ ] `config/settings.py` — INSTALLED_APPS + MEDIA
- [ ] `config/urls.py` — include movies.urls + static media
- [ ] `requirements.txt` — Pillow added
- [ ] `docs/movies-data-model-spec.md` — spec (fuente de verdad)
- [ ] `docs/lab05-admin-documentation.md` — este archivo
- [ ] `docs/screenshots/` — capturas (10+ archivos)

---

## 7. Known Issues / Decisions

- **Inline delete for editors**: Django admin inline `can_delete` se controla por `has_delete_permission` en el inline. El grupo editors no tiene `delete_rating` → inline no muestra checkbox delete. Comportamiento correcto.
- **Genre slug in URL**: Usamos `name|lower|slugify` en template para generar links. La vista usa `name__iexact` con replace `-` → ` ` para lookup tolerante.
- **Average rating calculation**: Hecho en Python en vista (loop sobre queryset annotate). Para escalar, mover a annotation con `Coalesce(Avg(...), 0)` y ordenar en BD.
- **No light mode**: Spec pide solo tema oscuro. Implementado.

---

> **Nota**: Todas las capturas deben guardarse en `docs/screenshots/` con nombres descriptivos. Este documento sigue el formato del Lab 4 para consistencia.
```

### 2. Crear directorio screenshots
```bash
mkdir -p docs/screenshots
```

### 3. Capturas requeridas (mínimo 10)
Tomar capturas de pantalla (Win+Shift+S o herramienta similar) y guardar en `docs/screenshots/`:

1. `admin-basic-genre.png`
2. `admin-basic-person.png`
3. `admin-basic-movie.png`
4. `admin-basic-rating.png`
5. `admin-custom-genre.png`
6. `admin-custom-person.png`
7. `admin-custom-movie.png`
8. `admin-custom-movie-inline.png`
9. `admin-custom-rating.png`
10. `permissions-group-editors.png`
11. `admin-superuser-movie-list.png`
12. `admin-editor-movie-list.png`
13. `view-recommendations-all.png`
14. `view-recommendations-genre.png`
15. `view-css-variables.png` (DevTools)

### 4. Verificar documentación
- Leer `docs/lab05-admin-documentation.md` completo.
- Confirmar que cada sección tiene: captura, código, explicación, casos de prueba.
- Verificar que la tabla de permisos coincide con lo probado.
- Confirmar formato idéntico a Lab 4 (revisar `docs/lab04-documentation.md` si existe).

## Reglas obligatorias
- **Formato idéntico** a Lab 4 (nombre alumno, título, captura, código, explicación, casos de prueba).
- Capturas en `docs/screenshots/` con nombres descriptivos.
- Código y comentarios en **INGLÉS**. Explicaciones al usuario en **ESPAÑOL**.
- Incluir tabla comparativa superusuario vs editor.
- Incluir resumen de casos de prueba (tabla).
- Ante duda sobre formato, **preguntar al usuario**.