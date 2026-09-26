from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    """Genre model for categorizing movies."""
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Person(models.Model):
    """Person model representing directors and actors."""
    ROLE_CHOICES = [
        ("director", "Director"),
        ("actor", "Actor"),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    photo = models.ImageField(upload_to="people/", blank=True, null=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    """Movie model with genre relationship."""
    title = models.CharField(max_length=200)
    release_year = models.PositiveSmallIntegerField()
    synopsis = models.TextField(blank=True)
    poster = models.ImageField(upload_to="movies/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ManyToMany for genres: A movie can have multiple genres, and a genre
    # can belong to multiple movies. This is a classic many-to-many relationship.
    genres = models.ManyToManyField(
        "Genre",
        related_name="movies",
        blank=True
    )

    class Meta:
        ordering = ["-release_year", "title"]

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Rating(models.Model):
    """Rating model for movie reviews with score validation."""
    movie = models.ForeignKey(
        "Movie",
        on_delete=models.CASCADE,
        related_name="ratings"
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Justification for on_delete=CASCADE:
    # A Rating has no meaning without its Movie. When a Movie is deleted,
    # its associated Ratings lose their context and should be removed.
    # This differs from the previous lab where PROTECT was used to preserve
    # referential integrity in a different context.

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.movie} — {self.score}/10"