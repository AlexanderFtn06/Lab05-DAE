---
description: "Create public recommendation view with dark cinema theme, custom CSS"
mode: subagent
tools:
  write: true
  edit: true
---

# movies-views

## Objetivo
Paso 10: Crear una vista pública de recomendación (películas del mismo género, ordenadas por mejor valoración promedio) con su URL y plantilla. Diseño visual: tema "cine oscuro" — fondo negro/gris oscuro (tipo #121212 o #1a1a1a), acentos dorados (#d4af37) o rojo cinematográfico (#b8323f) para títulos y elementos destacados, tarjetas de película con póster, título, año, género(s) y valoración promedio visible (por ejemplo con estrellas o un número destacado), tipografía clara con buen contraste sobre fondo oscuro, diseño responsive. Usa un archivo CSS propio (`movies/static/movies/style.css`), sin frameworks externos por CDN.

## Instrucciones

### 1. Crear directorio de static files
```bash
mkdir -p movies/static/movies
```

### 2. Crear CSS: movies/static/movies/style.css
```css
/* Dark Cinema Theme */
:root {
  --bg-primary: #121212;
  --bg-secondary: #1a1a1a;
  --bg-card: #1f1f1f;
  --accent-gold: #d4af37;
  --accent-red: #b8323f;
  --text-primary: #f5f5f5;
  --text-secondary: #b0b0b0;
  --text-muted: #808080;
  --border-color: #333;
  --shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  background-color: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

/* Header */
.site-header {
  text-align: center;
  padding: 3rem 1rem 2rem;
  border-bottom: 1px solid var(--border-color);
  background: linear-gradient(180deg, var(--bg-secondary) 0%, var(--bg-primary) 100%);
}

.site-title {
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 700;
  background: linear-gradient(135deg, var(--accent-gold) 0%, #f4d03f 50%, var(--accent-gold) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: 0.05em;
  margin-bottom: 0.5rem;
}

.site-tagline {
  color: var(--text-secondary);
  font-size: 1.1rem;
  font-weight: 300;
}

/* Movie Grid */
.movie-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

/* Movie Card */
.movie-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
}

.movie-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow);
  border-color: var(--accent-gold);
}

.movie-poster {
  width: 100%;
  aspect-ratio: 2/3;
  object-fit: cover;
  background: var(--bg-secondary);
}

.movie-poster-placeholder {
  width: 100%;
  aspect-ratio: 2/3;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--bg-secondary) 0%, #2a2a2a 100%);
  color: var(--text-muted);
  font-size: 3rem;
}

.movie-info {
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.movie-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 0.25rem;
  line-height: 1.3;
}

.movie-year {
  color: var(--text-muted);
  font-size: 0.9rem;
  margin-bottom: 0.75rem;
}

.movie-genres {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1rem;
}

.genre-tag {
  background: rgba(212, 175, 55, 0.15);
  color: var(--accent-gold);
  padding: 0.2rem 0.6rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 500;
  border: 1px solid rgba(212, 175, 55, 0.3);
}

.movie-rating {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding-top: 0.75rem;
  border-top: 1px solid var(--border-color);
  margin-top: auto;
}

.rating-stars {
  display: flex;
  gap: 0.15rem;
}

.star {
  color: var(--accent-gold);
  font-size: 1.1rem;
  line-height: 1;
}

.star.empty {
  color: var(--text-muted);
}

.rating-value {
  font-weight: 700;
  color: var(--accent-gold);
  font-size: 1.1rem;
  min-width: 2.5rem;
}

.rating-count {
  color: var(--text-muted);
  font-size: 0.8rem;
}

/* Section Header */
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--border-color);
}

.section-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--text-primary);
}

.genre-badge {
  background: linear-gradient(135deg, var(--accent-red) 0%, #c0392b 100%);
  color: white;
  padding: 0.4rem 1rem;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 500;
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: var(--text-secondary);
}

.empty-state-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
  opacity: 0.5;
}

/* Footer */
.site-footer {
  text-align: center;
  padding: 2rem;
  color: var(--text-muted);
  font-size: 0.85rem;
  border-top: 1px solid var(--border-color);
  margin-top: 3rem;
}

/* Responsive */
@media (max-width: 768px) {
  .container {
    padding: 1.5rem 0.75rem;
  }
  
  .movie-grid {
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 1.5rem;
  }
  
  .movie-info {
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .movie-grid {
    grid-template-columns: 1fr;
  }
}
```

### 3. Crear vista en movies/views.py
```python
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Count
from .models import Movie, Genre


def movie_recommendations(request, genre_slug=None):
    """
    Public recommendation view:
    - If genre_slug provided: show movies of that genre ordered by avg rating desc.
    - If no genre: show all movies ordered by avg rating desc.
    """
    genres = Genre.objects.annotate(movie_count=Count("movies")).filter(movie_count__gt=0)
    
    if genre_slug:
        genre = get_object_or_404(Genre, name__iexact=genre_slug.replace("-", " "))
        movies = Movie.objects.filter(genres=genre)
        section_title = f"Recommendations: {genre.name}"
        genre_badge = genre.name
    else:
        genre = None
        movies = Movie.objects.all()
        section_title = "Top Rated Movies"
        genre_badge = "All Genres"
    
    # Annotate with average rating and rating count
    movies = movies.annotate(
        avg_rating=Avg("ratings__score"),
        rating_count=Count("ratings")
    ).filter(rating_count__gt=0).order_by("-avg_rating", "-release_year")
    
    # Prepare rating data for template (stars)
    for movie in movies:
        if movie.avg_rating:
            movie.stars_full = int(movie.avg_rating / 2)  # 10-point to 5-star
            movie.stars_half = 1 if (movie.avg_rating / 2) - movie.stars_full >= 0.5 else 0
            movie.stars_empty = 5 - movie.stars_full - movie.stars_half
        else:
            movie.stars_full = movie.stars_half = movie.stars_empty = 0
    
    context = {
        "movies": movies,
        "genres": genres,
        "current_genre": genre,
        "section_title": section_title,
        "genre_badge": genre_badge,
    }
    return render(request, "movies/recommendations.html", context)
```

### 4. Crear plantilla: movies/templates/movies/recommendations.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if current_genre %}{{ current_genre.name }} - {% endif %}Movie Recommendations</title>
    <link rel="stylesheet" href="{% static 'movies/style.css' %}">
</head>
<body>
    <header class="site-header">
        <div class="container">
            <h1 class="site-title">🎬 Cinema Vault</h1>
            <p class="site-tagline">Discover your next favorite film</p>
        </div>
    </header>

    <main class="container">
        <nav aria-label="Genre navigation" style="margin-bottom: 2rem;">
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center;">
                <a href="{% url 'movie_recommendations' %}" 
                   class="genre-tag" style="text-decoration: none; display: inline-block; background: {% if not current_genre %}var(--accent-gold){% else %}rgba(212,175,55,0.15){% endif %}; color: {% if not current_genre %}var(--bg-primary){% else %}var(--accent-gold){% endif %}; border-color: {% if not current_genre %}var(--accent-gold){% else %}rgba(212,175,55,0.3){% endif %};">
                    All Genres
                </a>
                {% for g in genres %}
                <a href="{% url 'movie_recommendations_genre' g.name|lower|slugify %}" 
                   class="genre-tag" style="text-decoration: none; display: inline-block;">
                    {{ g.name }} ({{ g.movie_count }})
                </a>
                {% endfor %}
            </div>
        </nav>

        <div class="section-header">
            <h2 class="section-title">{{ section_title }}</h2>
            <span class="genre-badge">{{ genre_badge }}</span>
        </div>

        {% if movies %}
        <div class="movie-grid">
            {% for movie in movies %}
            <article class="movie-card">
                {% if movie.poster %}
                <img src="{{ movie.poster.url }}" alt="{{ movie.title }} poster" class="movie-poster" loading="lazy">
                {% else %}
                <div class="movie-poster-placeholder" aria-hidden="true">🎞️</div>
                {% endif %}
                <div class="movie-info">
                    <h3 class="movie-title">{{ movie.title }}</h3>
                    <p class="movie-year">{{ movie.release_year }}</p>
                    <div class="movie-genres">
                        {% for genre in movie.genres.all %}
                        <span class="genre-tag">{{ genre.name }}</span>
                        {% endfor %}
                    </div>
                    <div class="movie-rating">
                        <div class="rating-stars" aria-label="Rating: {{ movie.avg_rating|floatformat:1 }}/10">
                            {% for _ in ""|rjust:movie.stars_full %}<span class="star">★</span>{% endfor %}
                            {% if movie.stars_half %}<span class="star">½</span>{% endif %}
                            {% for _ in ""|rjust:movie.stars_empty %}<span class="star empty">★</span>{% endfor %}
                        </div>
                        <span class="rating-value">{{ movie.avg_rating|floatformat:1 }}</span>
                        <span class="rating-count">({{ movie.rating_count }} reviews)</span>
                    </div>
                </div>
            </article>
            {% endfor %}
        </div>
        {% else %}
        <div class="empty-state">
            <div class="empty-state-icon">🎬</div>
            <h3>No movies found</h3>
            <p>No rated movies available for this genre yet.</p>
        </div>
        {% endif %}
    </main>

    <footer class="site-footer">
        <div class="container">
            <p>Cinema Vault — Dark Theme Movie Recommendations</p>
        </div>
    </footer>
</body>
</html>
```

### 5. Configurar URLs en movies/urls.py
```python
from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.movie_recommendations, name="movie_recommendations"),
    path("genre/<slug:genre_slug>/", views.movie_recommendations, name="movie_recommendations_genre"),
]
```

### 6. Incluir en config/urls.py
En `config/urls.py` (verificar patrón de `library`):
```python
from django.urls import path, include
# ... existing imports

urlpatterns = [
    # ... existing patterns
    path("movies/", include("movies.urls")),
    # ...
]
```

### 7. Verificar
- `python manage.py check`
- `python manage.py runserver`
- Visitar `http://127.0.0.1:8000/movies/` → ver lista completa ordenada por rating.
- Visitar `http://127.0.0.1:8000/movies/genre/action/` → filtrado por género.
- Verificar responsive: redimensionar ventana, móvil.
- Verificar: pósters cargan, placeholders si no hay imagen, estrellas doradas, acentos dorados/rojos, fondo oscuro.

## Reglas obligatorias
- **No frameworks CSS externos** (Bootstrap, Tailwind, etc.). Solo `movies/static/movies/style.css`.
- Colores exactos: `#121212`/`#1a1a1a` fondo, `#d4af37` dorado, `#b8323f` rojo.
- Tarjetas con: póster, título, año, géneros (tags), rating promedio (estrellas + número).
- Responsive: grid auto-fill minmax(280px, 1fr).
- Código y comentarios en **INGLÉS**. Explicaciones al usuario en **ESPAÑOL**.
- Seguir `docs/movies-data-model-spec.md` (nombres de campos: `avg_rating`, `genres`, `poster`, etc.).
- Ante duda, **preguntar al usuario**.