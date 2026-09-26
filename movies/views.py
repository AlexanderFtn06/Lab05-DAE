from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Count
from django.utils.text import slugify
from .models import Movie, Genre, Rating


def movie_recommendations(request, genre_slug=None):
    """
    Public recommendation view:
    - If genre_slug provided: show movies of that genre ordered by avg rating desc.
    - If no genre: show all movies ordered by avg rating desc.
    """
    genres = Genre.objects.annotate(movie_count=Count("movies")).filter(movie_count__gt=0)
    
    if genre_slug:
        # Look up genre by slug field (handles accented names correctly)
        genre = get_object_or_404(Genre, slug=genre_slug)
        movies = Movie.objects.filter(genres=genre)
        section_title = f"Recomendaciones: {genre.name}"
        genre_badge = genre.name
    else:
        genre = None
        movies = Movie.objects.all()
        section_title = "Las Mejor Valoradas"
        genre_badge = "Todos los géneros"
    
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


def movie_detail(request, pk):
    """
    Movie detail view showing:
    - Title, year, synopsis, poster
    - All genres
    - Average rating
    - All individual ratings (score + comment)
    """
    movie = get_object_or_404(
        Movie.objects.prefetch_related("genres", "ratings"),
        pk=pk
    )
    
    # Calculate average rating
    ratings = movie.ratings.all()
    rating_count = ratings.count()
    
    if rating_count > 0:
        avg_rating = ratings.aggregate(avg=Avg("score"))["avg"]
        # Convert 1-10 scale to 5-star scale
        rating_5_scale = avg_rating / 2
        stars_full = int(rating_5_scale)
        stars_half = 1 if (rating_5_scale - stars_full) >= 0.5 else 0
        stars_empty = 5 - stars_full - stars_half
    else:
        avg_rating = None
        stars_full = stars_half = stars_empty = 0
    
    # Prepare individual ratings with star data
    ratings_with_stars = []
    for rating in ratings:
        score_5_scale = rating.score / 2
        rating.stars_full = int(score_5_scale)
        rating.stars_half = 1 if (score_5_scale - rating.stars_full) >= 0.5 else 0
        rating.stars_empty = 5 - rating.stars_full - rating.stars_half
        ratings_with_stars.append(rating)
    
    # Determine back URL (referer or genre-filtered list)
    back_url = request.META.get("HTTP_REFERER")
    if not back_url:
        # Default to recommendations list
        back_url = "/movies/"
    
    context = {
        "movie": movie,
        "ratings": ratings_with_stars,
        "rating_count": rating_count,
        "avg_rating": avg_rating,
        "stars_full": stars_full,
        "stars_half": stars_half,
        "stars_empty": stars_empty,
        "back_url": back_url,
    }
    return render(request, "movies/movie_detail.html", context)