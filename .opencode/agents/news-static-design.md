---
description: "Paso 10: cargar los estilos con {% load static %} y servir news/static/news/style.css y las imágenes correctamente. Diseño visual estilo \"revista editorial oscura\": fondo muy oscuro (tipo #0f0f10 o #141414), superficies un poco más claras (#1c1c1e), texto blanco hueso (#ececec), acentos naranja (#ff6b35) o coral (#ff7f6b) para categorías, enlaces y detalles; titulares en tipografía serif del sistema (Georgia o similar) y cuerpo en sans-serif del sistema; cabecera tipo cabecera de revista con navegación de categorías; portada con una noticia destacada grande y el resto en cuadrícula de tarjetas con imagen, categoría, fecha y resumen recortado; barra lateral en el bloque sidebar; hover suaves; diseño responsive; fallback visual (degradado) cuando una noticia no tiene imagen. Sin frameworks ni fuentes externas por CDN."
mode: subagent
tools:
  write: true
  edit: true
---

# news-static-design

## Instrucciones

Crear `news/static/news/style.css` con diseño "revista editorial oscura":

### Paleta de colores
- Fondo: `#0f0f10` o `#141414`
- Superficies: `#1c1c1e`
- Texto principal: `#ececec`
- Acentos: `#ff6b35` (naranja) / `#ff7f6b` (coral)
- Bordes sutiles: `#2c2c2e`

### Tipografía
- Titulares: `font-family: Georgia, "Times New Roman", serif;`
- Cuerpo: `font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;`

### Layout
- **Cabecera**: Estilo revista, nav de categorías horizontal, responsive (hamburger en móvil)
- **Portada**: 
  - Noticia destacada (hero) grande arriba
  - Grid de tarjetas (CSS Grid: `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))`)
- **Tarjetas**: Imagen (aspect-ratio 16:9), badge categoría (acento naranja), título, resumen, fecha, autor
- **Sidebar**: Widgets (categorías, últimas noticias, tags)
- **Detalle**: Imagen hero, cuerpo con buena legibilidad, meta (autor, categorías, fecha)
- **Hover**: Transiciones suaves (`transition: all 0.2s ease`), elevación en tarjetas
- **Responsive**: Breakpoints en 768px, 1024px
- **Fallback imagen**: Degradado CSS `background: linear-gradient(135deg, #1c1c1e 0%, #2c2c2e 100%)` cuando no hay `featured_image`

### En plantillas
- `{% load static %}` al inicio
- `<link rel="stylesheet" href="{% static 'news/style.css' %}">`
- Imágenes: `{{ article.featured_image.url }}` (servidas via MEDIA_URL)

## Reglas

- Sin frameworks CSS (Bootstrap, Tailwind, etc.)
- Sin fuentes externas por CDN
- Solo CSS nativo + variables CSS
- Código y comentarios en INGLÉS