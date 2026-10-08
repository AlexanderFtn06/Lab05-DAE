---
description: "Pasos 6, 7 y 8: escribir las vistas y las plantillas de portada, detalle de noticia y listado por categoría, todas heredando de news/base.html. La portada recorre las noticias con {% for %}, muestra el caso sin resultados con {% empty %} y aplica filtros de fecha (date) y de recorte (truncatewords) al resumen. El detalle muestra imagen, autor y categorías. El listado por categoría reutiliza el fragmento _article_card.html. Usar select_related/prefetch_related en las vistas. Si las rutas aún no existen, verificar el renderizado con render_to_string en el shell; no crear rutas provisionales, eso es el paso 9."
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# news-pages

## Instrucciones

### Vistas en `news/views.py`

1. **home** (portada):
   - Query: `Article.objects.select_related("author").prefetch_related("categories").filter(published_at__lte=timezone.now())[:10]`
   - Template: `news/home.html`
   - Context: `{"articles": articles}`

2. **article_detail**:
   - Query: `get_object_or_404(Article.objects.select_related("author").prefetch_related("categories"), slug=slug, published_at__lte=timezone.now())`
   - Template: `news/article_detail.html`
   - Context: `{"article": article}`

3. **category_detail**:
   - Query: `get_object_or_404(Category, slug=slug)`
   - Artículos: `category.articles.select_related("author").prefetch_related("categories").filter(published_at__lte=timezone.now())`
   - Template: `news/category_detail.html`
   - Context: `{"category": category, "articles": articles}`

### Plantillas (heredan de `news/base.html`)

**news/home.html** (portada):
- Bloque `content`: 
  - Noticia destacada (primera): tarjeta grande con imagen, título, resumen, autor, fecha, categorías
  - Resto: grid de tarjetas usando `{% for article in articles|slice:"1:" %}` + `{% include "news/_article_card.html" %}`
  - `{% empty %}`: "No hay noticias publicadas"
- Bloque `sidebar`: categorías con enlace a `category_detail`

**news/article_detail.html**:
- Imagen destacada (o fallback)
- Título, cuerpo completo (`linebreaks`), autor (con bio y foto), categorías (badges con enlaces), fecha
- Artículos relacionados (misma categoría, excluir actual)

**news/category_detail.html**:
- Título de categoría
- Grid de tarjetas: `{% for article in articles %}{% include "news/_article_card.html" %}{% empty %}Sin noticias{% endfor %}`

### Verificación (sin URLs aún)
- `python manage.py shell -c "from django.template.loader import render_to_string; from news.views import home; from django.test import RequestFactory; factory = RequestFactory(); request = factory.get('/'); print(render_to_string('news/home.html', home(request).context_data))"`

## Reglas

- `select_related` / `prefetch_related` obligatorios
- Filtros: `date`, `truncatewords`, `linebreaks`
- `{% for %}` / `{% empty %}`
- Sin `|safe` ni lógica de negocio
- Código y comentarios en INGLÉS