---
description: "Paso 10: cargar los estilos con {% load static %} y servir news/static/news/style.css y las imágenes correctamente. Diseño visual estilo \"revista editorial oscura\": fondo muy oscuro (tipo #0f0f10 o #141414), superficies un poco más claras (#1c1c1e), texto blanco hueso (#ececec), acentos naranja (#ff6b35) o coral (#ff7f6b) para categorías, enlaces y detalles; titulares en tipografía serif del sistema (Georgia o similar) y cuerpo en sans-serif del sistema; cabecera tipo cabecera de revista con navegación de categorías; portada con una noticia destacada grande y el resto en cuadrícula de tarjetas con imagen, categoría, fecha y resumen recortado; barra lateral en el bloque sidebar; hover suaves; diseño responsive; fallback visual (degradado) cuando una noticia no tiene imagen. Sin frameworks ni fuentes externas por CDN."
mode: subagent
tools:
  write: true
  edit: true
---

# news-static-design

## Objetivo
Implementar el diseño visual "revista editorial oscura" en `news/static/news/style.css` y asegurar que estáticos y medios se sirvan correctamente.

## Instrucciones
1. Crear `news/static/news/style.css` con:
   - **Paleta**: 
     - Fondo: `#0f0f10` o `#141414`
     - Superficies: `#1c1c1e`
     - Texto principal: `#ececec`
     - Acentos: `#ff6b35` (naranja) / `#ff7f6b` (coral)
   - **Tipografía**:
     - Titulares: `font-family: Georgia, "Times New Roman", serif;`
     - Cuerpo: `font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;`
   - **Layout**:
     - Cabecera tipo revista: logo + nav categorías (flex, responsive).
     - Portada: noticia destacada grande (hero) + grid de tarjetas (CSS Grid, `auto-fit`, `minmax(280px, 1fr)`).
     - Tarjeta (`_article_card.html`): imagen (aspect-ratio 16:9), badge categoría (acento naranja), título, resumen recortado, fecha, autor.
     - Sidebar: widgets en `aside` (categorías, noticias recientes).
     - Detalle: imagen hero, cuerpo con `linebreaks`, metadatos (autor, categorías, fecha).
   - **Interacciones**: hover suave en tarjetas (`transform: translateY(-4px)`, `box-shadow`), enlaces con transición de color.
   - **Responsive**: breakpoints en 768px y 1024px; grid a 1 columna en móvil, 2 en tablet, 3-4 en desktop.
   - **Fallback imagen**: degradado CSS (ej. `background: linear-gradient(135deg, #1c1c1e 0%, #2c2c2e 100%)`) en contenedor de imagen cuando no hay `featured_image`.
2. En `base.html`, confirmar `{% load static %}` y `<link rel="stylesheet" href="{% static 'news/style.css' %}">`.
3. Verificar que `collectstatic` funciona (en producción) y que en desarrollo `runserver` sirve los estáticos.
4. Las imágenes subidas via admin (`MEDIA_URL`) deben verse en plantillas con `{{ article.featured_image.url }}`.

## Reglas
- Código y comentarios en INGLÉS.
- **Sin frameworks CSS** (ni Bootstrap, Tailwind, etc.) ni fuentes externas por CDN.
- Solo CSS nativo, variables CSS (`--color-bg`, `--color-accent`, etc.) para mantener consistencia.
- Seguir `docs/news-data-model-spec.md` como única fuente de verdad.