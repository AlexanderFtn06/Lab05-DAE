---
description: "Pasos 6, 7 y 8: escribir las vistas y las plantillas de portada, detalle de noticia y listado por categoría, todas heredando de news/base.html. La portada recorre las noticias con {% for %}, muestra el caso sin resultados con {% empty %} y aplica filtros de fecha (date) y de recorte (truncatewords) al resumen. El detalle muestra imagen, autor y categorías. El listado por categoría reutiliza el fragmento _article_card.html. Usar select_related/prefetch_related en las vistas. Si las rutas aún no existen, verificar el renderizado con render_to_string en el shell; no crear rutas provisionales, eso es el paso 9."
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# news-pages

## Objetivo
Implementar vistas y plantillas para: portada (home), detalle de artículo y listado por categoría.

## Instrucciones

### 1. Vistas en `news/views.py`
- **home(request)**: 
  - Query: `Article.objects.select_related("author").prefetch_related("categories").all()[:10]` (o paginar luego).
  - Contexto: `{"articles": articles}`.
  - Template: `news/home.html`.
- **article_detail(request, slug)**:
  - Query: `Article.objects.select_related("author").prefetch_related("categories").get(slug=slug)`.
  - Contexto: `{"article": article}`.
  - Template: `news/article_detail.html`.
- **category_detail(request, slug)**:
  - Query: `Category.objects.prefetch_related("articles__author", "articles__categories").get(slug=slug)`.
  - Artículos: `category.articles.select_related("author").prefetch_related("categories").all()`.
  - Contexto: `{"category": category, "articles": articles}`.
  - Template: `news/category_detail.html`.

### 2. Plantillas (todas en `news/templates/news/`, heredando `{% extends "news/base.html" %}`)

#### `home.html` (portada)
- Bloque `content`: 
  - **Noticia destacada** (primer artículo): tarjeta grande con imagen, título, resumen, autor, fecha, categorías.
  - **Resto en cuadrícula**: `{% for article in articles|slice:"1:" %}` → `{% include "news/_article_card.html" with article=article %}`.
  - `{% empty %}`: mensaje "No hay noticias publicadas aún."
- Bloque `sidebar`: categorías con conteo (opcional), enlaces a `{% url 'news:category_detail' cat.slug %}`.

#### `article_detail.html`
- Bloque `content`: artículo completo con imagen destacada (o fallback), título, cuerpo (`{{ article.body|linebreaks }}`), autor (con bio y foto si hay), categorías (badges con enlaces), fecha.
- Bloque `sidebar`: artículos relacionados (misma categoría, excluyendo el actual), "Leer más".

#### `category_detail.html`
- Bloque `content`: título de categoría, descripción.
- Grid de tarjetas: `{% for article in articles %}{% include "news/_article_card.html" with article=article %}{% empty %}Sin noticias en esta categoría.{% endfor %}`.

### 3. Verificación sin rutas
- En shell: `python manage.py shell -c "from django.template.loader import render_to_string; from news.views import home; from django.http import HttpRequest; req = HttpRequest(); print(render_to_string('news/home.html', home(req).context_data))"` (adaptar según implementación).
- No crear URLs todavía (paso 9).

## Reglas
- Código y comentarios en INGLÉS.
- Usar `select_related` / `prefetch_related` para evitar N+1.
- Filtros en plantilla: `date`, `truncatewords`, `linebreaks`.
- `{% for %}` / `{% empty %}` en bucles.
- Sin `|safe` ni lógica de negocio.
- Seguir `docs/news-data-model-spec.md` como única fuente de verdad.