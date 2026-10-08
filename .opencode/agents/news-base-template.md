---
description: "Paso 4: escribir templates/news/base.html con la estructura común del portal (cabecera, navegación, pie) y los bloques title, content y sidebar que las páginas rellenarán."
mode: subagent
tools:
  write: true
  edit: true
---

# news-base-template

## Objetivo
Crear la plantilla base `templates/news/base.html` con la estructura común del portal de noticias.

## Instrucciones
1. Crear el archivo `templates/news/base.html` (directorio `templates/` en la raíz del proyecto).
2. Estructura HTML5 completa con:
   - `<head>`: meta charset, viewport, título con bloque `{% block title %}News Portal{% endblock %}`, carga de estáticos con `{% load static %}`, enlace a `news/static/news/style.css`.
   - `<body>`: 
     - **Cabecera** (`<header>`): nombre del portal, navegación principal con enlaces a categorías (usar `{% url 'news:home %}` y URLs de categorías dinámicas si aplica).
     - **Contenido principal** (`<main>`): bloque `{% block content %}{% endblock %}`.
     - **Barra lateral** (`<aside>`): bloque `{% block sidebar %}{% endblock %}` (opcional, para widgets futuros).
     - **Pie** (`<footer>`): copyright, enlaces legales.
3. Usar clases CSS semánticas para que `news-static-design` pueda estilizar luego.
4. Todas las plantillas de `news` heredarán de esta con `{% extends "news/base.html" %}`.

## Reglas
- Código y comentarios en INGLÉS.
- Plantilla en `templates/news/base.html` (prefijo `news/` para no pisar `library/templates/base.html`).
- Sin lógica de negocio; solo estructura y bloques.
- Seguir `docs/news-data-model-spec.md` como única fuente de verdad.