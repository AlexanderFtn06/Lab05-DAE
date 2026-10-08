---
description: "Paso 13: redactar el entregable en español con el formato del curso (nombre del alumno, título del desarrollo, captura del resultado, código, explicación y casos de prueba, más una captura de la estructura del proyecto en el editor), con una sección de observaciones que explique la estructura de plantillas (base, fragmento, páginas) y por qué se reutiliza el marcado."
mode: subagent
tools:
  read: true
  write: true
---

# news-documentation

## Instrucciones

Redactar entregable en `docs/lab06-entregable.md` (formato del curso, en ESPAÑOL):

### Estructura obligatoria

1. **Datos del alumno**: Nombre, título "Laboratorio 6 - Motor de plantillas con Django"

2. **Captura del resultado**: Screenshots del portal funcionando:
   - Portada (`/news/`)
   - Detalle de noticia (`/news/article/<slug>/`)
   - Listado por categoría (`/news/category/<slug>/`)
   - Admin con datos cargados

3. **Código relevante** (extractos clave):
   - `news/models.py`
   - `news/views.py`
   - `news/urls.py` + include en `config/urls.py`
   - `templates/news/base.html`
   - `news/templates/news/_article_card.html`
   - `news/templates/news/home.html`
   - `news/templates/news/article_detail.html`
   - `news/templates/news/category_detail.html`
   - `news/static/news/style.css` (variables CSS, grid, fallback)
   - `news/admin.py`

4. **Explicación**: Qué hace cada componente, cómo se relacionan, uso de `select_related`/`prefetch_related`, herencia de plantillas, fragmento reutilizable, filtros (`date`, `truncatewords`, `linebreaks`), URLs con `{% url %}`, estilos CSS.

5. **Casos de prueba** (tabla):
   | Caso | Entrada | Resultado esperado |
   |------|---------|-------------------|
   | Portada sin noticias | BD vacía | "No hay noticias publicadas" |
   | Portada con noticias | 6 artículos | Hero + grid 5 tarjetas |
   | Detalle artículo | slug válido | Imagen, título, cuerpo, autor, categorías, fecha |
   | Detalle artículo | slug inválido | 404 |
   | Categoría | slug válido | Lista filtrada con include |
   | Categoría vacía | slug sin artículos | "Sin noticias en esta categoría" |
   | Escapado HTML | Body con `<script>` | Texto plano, no ejecuta |
   | Admin | Superusuario | CRUD completo, slugs auto, filtros |

6. **Captura estructura del proyecto**: Tree view en editor mostrando:
   ```
   config/
   library/
   movies/
   news/
   ├── migrations/
   ├── static/news/style.css
   ├── templates/news/
   │   ├── base.html
   │   ├── _article_card.html
   │   ├── home.html
   │   ├── article_detail.html
   │   └── category_detail.html
   ├── admin.py
   ├── models.py
   ├── urls.py
   └── views.py
   templates/
   └── news/
       └── base.html
   static/
   └── news/
       └── style.css
   media/
   └── authors/, articles/
   ```

7. **Observaciones** (sección obligatoria):
   - Explicar estructura de plantillas: `base.html` (layout global, bloques title/content/sidebar), `_article_card.html` (fragmento reutilizable), páginas hijas (home, detail, category)
   - Por qué se reutiliza el marcado: DRY, consistencia, mantenimiento único, separación presentación/lógica
   - Separación responsabilidades: modelos, vistas (queries optimizadas), plantillas (solo presentación), CSS (estilos)
   - Seguridad: autoescape activo, sin `|safe`, `on_delete=PROTECT`

## Reglas

- Documento en ESPAÑOL
- Código en INGLÉS
- Formato Markdown
- Seguir `docs/news-data-model-spec.md` como única fuente de verdad