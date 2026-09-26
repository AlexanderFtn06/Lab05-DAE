from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Count
from django.utils.text import slugify
from .models import Movie, Genre


def movie_recommendations(request, genre_slug=None):
    """
    Public recommendation view:
    - If genre_slug provided: show movies of that genre ordered by avg rating desc.
    - If no genre: show all movies ordered by avg rating desc.
    """
    genres = Genre.objects.annotate(movie_count=Count("movies")).filter(movie_count__gt=0)
    
    if genre_slug:
        # Convert slug back to genre name (replace hyphens with spaces, case-insensitive lookup)
        genre_name = genre_slug.replace("-", " ")
        genre = get_object_or_404(Genre, name__iexact=genre_name)
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
    
    # Prepare rating data for template (stars) - converting 10-point scale to 5-star
    for movie in movies:
        if movie.avg_rating:
            # Convert 1-10 scale to 5-star scale (divide by 2)
            rating_5_scale = movie.avg_rating / 2
            movie.stars_full = int(rating_5_scale)
            movie.stars_half = 1 if (rating_5_scale - movie.stars_full) >= 0.5 else 0
            movie.stars_empty = 5 - movie.stars_full - movie.stars_half
        else:
            movie.stars_full = movie.stars_half = movie.stars_empty = 0
    
    context = {
        "movies": movies,
        "genres": genres,
        "current_genre": genre,
        "current_genre_slug": genre_slug,
        "section_title": section_title,
        "genre_badge": genre_badge,
    }
    return render(request, "movies/recommendations.html", context)