# News App Data Model Specification

**Laboratorio 6 – Motor de plantillas con Django**  
Única fuente de verdad para la app `news`. No modificar `library` ni `movies`.

---

## MODELOS

### Author
| Campo | Tipo | Opciones |
|-------|------|----------|
| `first_name` | CharField | max_length=100 |
| `last_name` | CharField | max_length=100 |
| `bio` | TextField | blank=True |
| `photo` | ImageField | upload_to="authors/", blank=True, null=True |

**Meta:** `ordering = ["last_name"]`  
**__str__:** `"first_name last_name"`

---

### Category
| Campo | Tipo | Opciones |
|-------|------|----------|
| `name` | CharField | max_length=100, unique=True |
| `slug` | SlugField | unique=True |
| `description` | TextField | blank=True |

**Meta:** `ordering = ["name"]`, `verbose_name_plural = "categories"`  
**__str__:** `name`

---

### Article
| Campo | Tipo | Opciones |
|-------|------|----------|
| `title` | CharField | max_length=200 |
| `slug` | SlugField | unique=True |
| `summary` | TextField | |
| `body` | TextField | |
| `featured_image` | ImageField | upload_to="articles/", blank=True, null=True |
| `published_at` | DateTimeField | default=timezone.now |

**Relaciones:**
- `author` → ForeignKey a `Author`, `on_delete=PROTECT`, `related_name="articles"`  
  *Justificación:* Borrar un autor no debe arrastrar sus noticias publicadas.
- `categories` → ManyToManyField a `Category`, `related_name="articles"`

**Meta:** `ordering = ["-published_at"]`  
**__str__:** `title`

---

## PLANTILLAS (nombres exactos y ubicación)

Directorio de plantillas del proyecto: `templates/` en la raíz, agregado a `DIRS` en `settings.py` (`APP_DIRS` se queda en `True`).

> **IMPORTANTE:** `library` ya tiene `library/templates/base.html` sin prefijo. Para no pisarlo, **todas las plantillas de esta app llevan el prefijo `news/`**:

| Archivo | Descripción |
|---------|-------------|
| `templates/news/base.html` | Layout común; bloques: `title`, `content`, `sidebar` |
| `news/templates/news/_article_card.html` | Fragmento de tarjeta, se incluye con `{% include %}` |
| `news/templates/news/home.html` | Portada |
| `news/templates/news/article_detail.html` | Detalle de noticia |
| `news/templates/news/category_detail.html` | Listado por categoría |

Todas las páginas heredan con `{% extends "news/base.html" %}`.

---

## RUTAS

`app_name = "news"`, prefijo `/news/` en `config/urls.py`; **el include de `news` debe ir ANTES de los includes de la raíz de `movies` y `library`**.

| Patrón | Nombre |
|--------|--------|
| `/news/` | `home` |
| `/news/article/<slug:slug>/` | `article_detail` |
| `/news/category/<slug:slug>/` | `category_detail` |

Todos los enlaces internos con `{% url 'news:...' %}`; **ninguna dirección escrita a mano**.

---

## ESTÁTICOS Y MEDIOS

- Hoja de estilos: `news/static/news/style.css`, cargada con `{% load static %}`.
- Reutilizar `MEDIA_URL`/`MEDIA_ROOT` ya configurados; **no duplicarlos**.

---

## CONTENIDO DE PRUEBA (Paso 11)

- 3 categorías: **Tecnología**, **Deportes**, **Cultura**
- 2 autores
- 6 noticias (2 por categoría, con al menos una noticia en dos categorías)

---

## REGLAS DE PLANTILLA

- Sin lógica de negocio en las plantillas: solo variables, `for`/`empty`, `if` y filtros (`date`, `truncatewords`).
- **Nunca** usar `|safe` ni `autoescape off` en el cuerpo de la noticia; el escapado automático de Django debe permanecer activo.