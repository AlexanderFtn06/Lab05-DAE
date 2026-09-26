from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.movie_recommendations, name="movie_recommendations"),
    path("genre/<slug:genre_slug>/", views.movie_recommendations, name="movie_recommendations_genre"),
]