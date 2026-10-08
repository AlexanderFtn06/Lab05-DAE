---
description: "Paso 5: crear el fragmento news/templates/news/_article_card.html con la tarjeta de una noticia, listo para incluirse con {% include %} desde la portada y desde el listado por categoría. Debe manejar el caso de noticia sin imagen destacada."
mode: subagent
tools:
  write: true
  edit: true
---

# news-partials

## Objetivo
Crear el fragmento reutilizable `news/templates/news/_article_card.html` para mostrar una tarjeta de noticia.

## Instrucciones
1. Crear el archivo `news/templates/news/_article_card.html` (dentro de la app `news`, **no** en `templates/` raíz).
2. Estructura de la tarjeta:
   - Imagen destacada: si `article.featured_image` existe, mostrar `<img src="{{ article.featured_image.url }}" alt="{{ article.title }}">`; si no, mostrar un **fallback visual** (degradado CSS o placeholder inline) — sin frameworks ni CDN.
   - Categoría principal: primera categoría de `article.categories.all` (badge con color naranja/coral).
   - Título: enlace a `{% url 'news:article_detail' article.slug %}`.
   - Resumen: `{{ article.summary|truncatewords:30 }}`.
   - Fecha: `{{ article.published_at|date:"d M Y" }}`.
   - Autor: `{{ article.author.first_name }} {{ article.author.last_name }}` (enlace opcional).
3. Usar `{% load static %}` si se referencia algún asset estático en el fallback.
4. Diseñado para ser incluido con `{% include "news/_article_card.html" with article=article %}` desde `home.html` y `category_detail.html`.
5. Clases CSS preparadas para el estilo "revista editorial oscura" del paso 10.

## Reglas
- Código y comentarios en INGLÉS.
- Manejar explícitamente el caso `featured_image` vacío (fallback visual).
- Sin lógica de negocio; solo variables, `if` y filtros.
- Seguir `docs/news-data-model-spec.md` como única fuente de verdad.