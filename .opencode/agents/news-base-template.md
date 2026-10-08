---
description: "Paso 4: escribir templates/news/base.html con la estructura común del portal (cabecera, navegación, pie) y los bloques title, content y sidebar que las páginas rellenarán."
mode: subagent
tools:
  write: true
  edit: true
---

# news-base-template

## Instrucciones

Crear `templates/news/base.html` (en la carpeta `templates/` de la raíz del proyecto, con prefijo `news/` para no pisar `library/templates/base.html`):

Estructura requerida:
- `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`
- **Cabecera** (`<header>`): Título del portal, navegación principal (enlaces a home, categorías)
- **Contenido principal** (`<main>`): Bloque `{% block content %}{% endblock %}`
- **Barra lateral** (`<aside>`): Bloque `{% block sidebar %}{% endblock %}` (opcional, para widgets)
- **Pie** (`<footer>`): Copyright, enlaces legales
- **Bloques obligatorios**:
  - `{% block title %}News Portal{% endblock %}` - en `<title>`
  - `{% block content %}{% endblock %}` - contenido principal
  - `{% block sidebar %}{% endblock %}` - barra lateral
- Cargar estáticos: `{% load static %}` al inicio
- Enlazar CSS: `<link rel="stylesheet" href="{% static 'news/style.css' %}">`

## Reglas

- Todas las plantillas de news usan prefijo `news/`
- Herencia: `{% extends "news/base.html" %}`
- Código y comentarios en INGLÉS
- No lógica de negocio en plantillas