---
description: "Paso 13: redactar el entregable en español con el formato del curso (nombre del alumno, título del desarrollo, captura del resultado, código, explicación y casos de prueba, más una captura de la estructura del proyecto en el editor), con una sección de observaciones que explique la estructura de plantillas (base, fragmento, páginas) y por qué se reutiliza el marcado."
mode: subagent
tools:
  read: true
  write: true
---

# news-documentation

## Objetivo
Redactar el entregable final del laboratorio 6 en formato del curso.

## Instrucciones
Crear un archivo Markdown (ej. `docs/lab06-entregable.md`) con la siguiente estructura:

### 1. Datos del alumno
- Nombre: [Tu nombre]
- Título: "Laboratorio 6 – Motor de plantillas con Django (app news)"

### 2. Captura del resultado
- Pantallazo(s) del portal funcionando: portada (`/news/`), detalle (`/news/article/<slug>/`), categoría (`/news/category/<slug>/`), admin con datos.

### 3. Código relevante
- `news/models.py` (modelos)
- `news/views.py` (vistas)
- `news/urls.py` + include en `config/urls.py`
- `templates/news/base.html`
- `news/templates/news/_article_card.html`
- `news/templates/news/home.html`
- `news/templates/news/article_detail.html`
- `news/templates/news/category_detail.html`
- `news/static/news/style.css` (extractos clave)
- `news/admin.py`

### 4. Explicación
- Qué hace cada componente y cómo se relacionan.
- Uso de `select_related` / `prefetch_related`.
- Herencia de plantillas (`extends "news/base.html"`).
- Fragmento reutilizable (`include "news/_article_card.html"`).
- Filtros usados: `date`, `truncatewords`, `linebreaks`.
- URLs con `{% url 'news:...' %}`.
- Estilos: variables CSS, diseño responsive, fallback de imagen.

### 5. Casos de prueba
| Caso | Entrada | Resultado esperado |
|------|---------|-------------------|
| Portada sin noticias | BD vacía | Mensaje "No hay noticias publicadas aún." |
| Portada con noticias | 6 artículos | Hero + grid 5 tarjetas |
| Detalle artículo | slug válido | Imagen, título, cuerpo, autor, categorías, fecha |
| Detalle artículo | slug inválido | 404 |
| Categoría | slug válido | Lista filtrada, tarjetas con include |
| Categoría vacía | slug sin artículos | "Sin noticias en esta categoría." |
| Escapado HTML | Body con `<script>` | Se muestra como texto, no ejecuta |
| Admin | Superusuario | CRUD completo, slugs auto, filtros |

### 6. Captura de estructura del proyecto
- Árbol de directorios en el editor (VS Code / PyCharm) mostrando:
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

### 7. Observaciones (sección obligatoria)
Explicar:
- **Estructura de plantillas**: `base.html` define layout global (header, main, aside, footer) y bloques `title`, `content`, `sidebar`. Las páginas (`home.html`, `article_detail.html`, `category_detail.html`) heredan y rellenan solo lo necesario.
- **Fragmento `_article_card.html`**: encapsula la tarjeta de noticia; se incluye con `{% include %}` en portada y listado por categoría → **DRY**, mantenimiento único, consistencia visual.
- **Por qué se reutiliza el marcado**: evita duplicación, garantiza que cambios en la tarjeta (ej. añadir badge de "nuevo") se reflejan en todas partes, separa presentación de lógica de vista.
- **Separación de responsabilidades**: modelos en `models.py`, consultas optimizadas en `views.py`, presentación en plantillas, estilos en CSS estático.
- **Seguridad**: escapado automático activo, sin `|safe` en plantillas, `on_delete=PROTECT` en autor.

## Reglas
- Documento en ESPAÑOL.
- Código en INGLÉS.
- Formato Markdown limpio.
- Seguir `docs/news-data-model-spec.md` como única fuente de verdad.