---
description: "Paso 5: crear el fragmento news/templates/news/_article_card.html con la tarjeta de una noticia, listo para incluirse con {% include %} desde la portada y desde el listado por categoría. Debe manejar el caso de noticia sin imagen destacada."
mode: subagent
tools:
  write: true
  edit: true
---

# news-partials

## Instrucciones

Crear `news/templates/news/_article_card.html` (fragmento reutilizable):

Estructura de la tarjeta:
- **Imagen destacada**: 
  - Si `article.featured_image` existe: `<img src="{{ article.featured_image.url }}" alt="{{ article.title }}">`
  - Si NO existe: mostrar fallback visual (degradado CSS o placeholder)
- **Categoría**: Badge con la primera categoría (`article.categories.first`)
- **Título**: Enlace a detail: `<a href="{% url 'news:article_detail' article.slug %}">{{ article.title }}</a>`
- **Resumen**: `{{ article.summary|truncatewords:30 }}`
- **Fecha**: `{{ article.published_at|date:"d M Y" }}`
- **Autor**: `{{ article.author.first_name }} {{ article.author.last_name }}`

Uso: `{% include "news/_article_card.html" with article=article %}`

## Reglas

- Manejar caso sin imagen (fallback visual)
- Solo variables, etiquetas de control (`if`, `for`) y filtros
- Sin lógica de negocio
- Código y comentarios en INGLÉS