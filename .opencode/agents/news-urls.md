---
description: "Paso 9: declarar app_name="news" y las tres rutas con los nombres del spec, incluirlas en config/urls.py bajo /news/ ANTES de los includes de la raíz, y reemplazar cualquier dirección escrita a mano por {% url 'news:...' %}."
mode: subagent
tools:
  write: true
  edit: true
---

# news-urls

## Objetivo
Configurar el enrutamiento de la app `news` y conectarla al proyecto principal.

## Instrucciones
1. Crear `news/urls.py`:
   ```python
   from django.urls import path
   from . import views

   app_name = "news"

   urlpatterns = [
       path("", views.home, name="home"),
       path("article/<slug:slug>/", views.article_detail, name="article_detail"),
       path("category/<slug:slug>/", views.category_detail, name="category_detail"),
   ]
   ```
2. En `config/urls.py`:
   - Importar `include` de `django.urls`.
   - Agregar `path("news/", include("news.urls"))` **ANTES** de los includes de `library` y `movies` (raíz).
   - Verificar que el servicio de medios (`static(settings.MEDIA_URL, ...)`) siga al final.
3. Revisar todas las plantillas (`home.html`, `article_detail.html`, `category_detail.html`, `_article_card.html`, `base.html`) y reemplazar cualquier URL escrita a mano por `{% url 'news:home' %}`, `{% url 'news:article_detail' article.slug %}`, `{% url 'news:category_detail' category.slug %}`.
4. Probar que las URLs resuelven: `python manage.py shell -c "from django.urls import reverse; print(reverse('news:home')); print(reverse('news:article_detail', args=['test-slug'])); print(reverse('news:category_detail', args=['tecnologia']))"`.

## Reglas
- Código y comentarios en INGLÉS.
- `app_name = "news"` obligatorio.
- Include en `config/urls.py` **antes** de los de la raíz.
- Todas las URLs internas con `{% url 'news:...' %}`.
- Seguir `docs/news-data-model-spec.md` como única fuente de verdad.