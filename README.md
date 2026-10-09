# Cinema Vault + Meridiano News
## Autor
Alexander Faustino

Proyecto acumulativo de los laboratorios 5 y 6 del curso **Desarrollo de Aplicaciones Empresariales**:

- **Lab 5** — "Administrador con Django": app `movies` (catálogo de películas con admin personalizado y permisos).
- **Lab 6** — "Motor de plantillas con Django": app `news` (portal de noticias "Meridiano" con herencia de plantillas, fragmentos reutilizables y diseño editorial oscuro).

---

## Descripción

El proyecto tiene **tres apps** que conviven sin modificarse entre sí:

| App | Responsabilidad | URLs |
|-----|----------------|------|
| `library` | Catálogo de libros, autores, editoriales y categorías (labs previos) | `/library/` |
| `movies` | Catálogo de películas, géneros, personas y valoraciones (Lab 5) | `/`, `/genre/<slug>/`, `/<id>/` |
| `news` | Portal de noticias "Meridiano" con plantillas, estilos y admin (Lab 6) | `/news/`, `/news/article/<slug>/`, `/news/category/<slug>/` |

### Apps públicas (sin login)

| App | Qué muestra |
|-----|-------------|
| **Movies** | Listado de películas ordenadas por valoración promedio, filtro por género, detalle con sinopsis, géneros y reseñas. |
| **News (Meridiano)** | Portada con noticia destacada + grid de tarjetas, detalle de artículo con imagen/autor/categorías/cuerpo, listado por categoría, diseño "revista editorial oscura" (fondo #0f0f10, acento naranja #ff6b35, tipografía serif/sans-serif, responsive). |

### Panel de administración (`/admin/`)

- **Movies**: 4 modelos (`Movie`, `Genre`, `Person`, `Rating`) con `ModelAdmin` personalizado, inline de valoraciones, filtros, búsqueda, `filter_horizontal`, campos de solo lectura.
- **News**: 3 modelos (`Author`, `Category`, `Article`) con `list_display` (incluye conteos eficientes), `list_filter`, `search_fields`, `prepopulated_fields` (slug auto), `filter_horizontal` para categorías, `date_hierarchy`.
- **Permisos**: grupo "editors" (Lab 5) con add/change en Movie, sin delete; superusuario original preservado.

---

## Modelo de datos — News (Lab 6)

| Modelo | Campos clave | Relaciones |
|--------|--------------|------------|
| `Author` | `first_name`, `last_name`, `bio`, `photo` | — |
| `Category` | `name` (unique), `slug` (unique), `description` | — |
| `Article` | `title`, `slug` (unique), `summary`, `body`, `featured_image`, `published_at` | `author` → FK `Author` (`PROTECT`, `related_name="articles"`); `categories` → M2M `Category` (`related_name="articles"`) |

> Justificación: `PROTECT` evita borrar un autor con artículos publicados; M2M permite que un artículo esté en varias categorías y viceversa.

Esquema completo en [`docs/news-data-model-spec.md`](docs/news-data-model-spec.md).

---

## Capacidades demostradas (Lab 6)

1. **Motor de plantillas con herencia y fragmentos**: `base.html` (bloques `title`, `content`, `sidebar`), fragmento `_article_card.html` reutilizado en portada y listado por categoría.
2. **Datos en plantillas sin lógica de negocio**: variables, `for`/`empty`, `if`, filtros `date`, `truncatewords`, `linebreaks`; **sin `|safe` ni `autoescape off`**.
3. **Gestión de contenido desde el admin**: 3 categorías, 2 autores, 6 noticias (2 por categoría, al menos 1 en 2 categorías) dadas de alta en `/admin/news/` y publicadas en el portal.
4. **Escapado automático verificado**: HTML en body se muestra como texto plano (entidades); contraste con `|safe` solo documentado en shell.

---

## Estructura de plantillas (News)

```
templates/
└── news/
    └── base.html              # Layout global: header, nav, main(content+sidebar), footer
news/
└── templates/
    └── news/
        ├── base.html          # (no existe, hereda de templates/news/base.html)
        ├── _article_card.html # Fragmento reutilizable (include)
        ├── home.html          # Portada: hero + grid + empty-state
        ├── article_detail.html# Detalle: imagen, meta, categorías, body|linebreaks, author-box
        └── category_detail.html # Listado por categoría: reutiliza _article_card.html
```

**Por qué reutilizar `_article_card.html`**: DRY, consistencia visual, mantenimiento único, separación presentación/lógica.

---

## Estilos (Lab 6 — Paso 10)

- **Archivo**: `news/static/news/style.css` (cargado con `{% load static %}`)
- **Diseño**: "Revista editorial oscura"
  - Fondo `#0f0f10`, superficies `#1c1c1e`, texto `#ececec`, acento `#ff6b35`/`#ff7f6b`
  - Titulares en **serif** (Georgia), cuerpo en **sans-serif** del sistema
  - Cabecera tipo revista, hero + grid responsive (`auto-fill, minmax(280px, 1fr)`)
  - Tarjetas con hover elevation, categorías como badges naranja
  - Fallback degradado cuando no hay imagen destacada
  - **Sin frameworks ni fuentes externas por CDN**

---

## Metodología (OpenCode)

Desarrollado con **sub-agentes especializados** (`.opencode/agents/`):

| Sub-agente | Laboratorio | Encargado de |
|------------|-------------|--------------|
| `news-project-structure` | 6 | Crear app `news`, instalar Pillow, `INSTALLED_APPS` |
| `news-settings` | 6 | `TEMPLATES[DIRS]`, estáticos, medios (sin duplicar) |
| `news-models` | 6 | Modelos `Author`, `Category`, `Article` + migraciones |
| `news-base-template` | 6 | `templates/news/base.html` con bloques |
| `news-partials` | 6 | `news/templates/news/_article_card.html` |
| `news-pages` | 6 | Vistas y plantillas: home, detail, category |
| `news-urls` | 6 | `app_name="news"`, 3 rutas, include en `config/urls.py` ANTES de raíz |
| `news-static-design` | 6 | `news/static/news/style.css` diseño oscuro responsive |
| `news-admin` | 6 | `ModelAdmin` personalizado + carga de 6 noticias |
| `news-escaping` | 6 | Prueba autoescape + documentación |
| `news-documentation` | 6 | Entregable formato curso |

*(Los sub-agentes de `movies-*` y `django-*` corresponden a labs previos y se mantienen intactos.)*

---

## Instalación y uso

```bash
# 1. Clonar
git clone <url-del-repositorio>
cd Lab04-DAE

# 2. Entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux / macOS

# 3. Dependencias
pip install -r requirements.txt

# 4. Migraciones
python manage.py migrate

# 5. Superusuario (si no existe)
python manage.py createsuperuser

# 6. Servidor
python manage.py runserver
```

### URLs principales

| App | URL | Descripción |
|-----|-----|-------------|
| Movies | `http://127.0.0.1:8000/` | Catálogo público películas |
| Movies | `http://127.0.0.1:8000/genre/<slug>/` | Filtrado por género |
| Movies | `http://127.0.0.1:8000/<id>/` | Detalle película |
| News | `http://127.0.0.1:8000/news/` | Portada Meridiano |
| News | `http://127.0.0.1:8000/news/article/<slug>/` | Detalle noticia |
| News | `http://127.0.0.1:8000/news/category/<slug>/` | Listado por categoría |
| Admin | `http://127.0.0.1:8000/admin/` | Panel de administración |
| Library | `http://127.0.0.1:8000/library/` | Catálogo libros (labs previos) |

---

## Capturas de funcionamiento — News (Lab 6)

### Portal público "Meridiano"

**1. Portada `/news/`** — Hero (noticia destacada) + grid de tarjetas + sidebar categorías

**2. Detalle `/news/article/<slug>/`** — Imagen, título, meta (fecha/autor), categorías (links), cuerpo con párrafos, author-box, "Volver a la portada"

**3. Categoría `/news/category/tecnologia/`** — 2 noticias, reutiliza `_article_card.html`

**4. Categoría `/news/category/cultura/`** — 2 noticias (1 compartida con Tecnología)

**5. Categoría `/news/category/deportes/`** — 2 noticias

**6. Responsive** — Vista móvil (1 columna), tablet (2), desktop (3-4)

### Admin News

**7. Listado Articles** — Columnas: título, autor, fecha, categorías, imagen; filtros laterales

**8. Listado Categories** — name, slug, noticias (anotado eficiente)

**9. Listado Authors** — Nombre completo, noticias (anotado eficiente)

**10. Formulario Article** — prepopulated slug, filter_horizontal categories, date_hierarchy

### Escapado automático (Paso 12)

**11. Noticia de prueba con HTML** — Se renderiza como texto plano (entidades `<script>...`)

**12. Shell con `|safe`** — Contraste documentado (solo en docs, nunca en plantillas)

### Estructura del proyecto

**13. Árbol en editor** — `news/`, `templates/news/`, `news/templates/news/`, `news/static/news/`, `media/articles/`

---

## Licencia

Proyecto educativo — Curso Desarrollo de Aplicaciones Empresariales.