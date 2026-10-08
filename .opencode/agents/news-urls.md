---
description: "Paso 9: declarar app_name="news" y las tres rutas con los nombres del spec, incluirlas en config/urls.py bajo /news/ ANTES de los includes de la raíz, y reemplazar cualquier dirección escrita a mano por {% url 'news:...' %}."
mode: subagent
tools:
  write: true
  edit: true
---

# news-urls

## Instrucciones

### 1. Crear `news/urls.py`
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

### 2. Incluir en `config/urls.py`
- Importar: `from django.urls import include`
- Agregar **ANTES** de los includes de la raíz (library, movies):
  ```python
  path("news/", include("news.urls")),
  ```

### 3. Reemplazar URLs hardcodeadas en plantillas
- `href="/news/"` → `href="{% url 'news:home' %}"`
- `href="/news/article/{{ article.slug }}/"` → `href="{% url 'news:article_detail' article.slug %}"`
- `href="/news/category/{{ category.slug }}/"` → `href="{% url 'news:category_detail' category.slug %}"`

### 4. Verificar
- `python manage.py check`
- `python manage.py shell -c "from django.urls import reverse; print(reverse('news:home')); print(reverse('news:article_detail', args=['test-slug'])); print(reverse('news:category_detail', args=['tecnologia']))"`

## Reglas

- `app_name = "news"` obligatorio
- Include en config/urls.py ANTES de los de la raíz
- Todas las URLs con `{% url 'news:...' %}`
- Código y comentarios en INGLÉS