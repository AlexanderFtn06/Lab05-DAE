from django.contrib import admin
from django.utils.html import format_html
from .models import Genre, Person, Movie, Rating


class RatingInline(admin.TabularInline):
    """Inline for managing ratings within the Movie admin."""
    model = Rating
    extra = 1
    readonly_fields = ("created_at",)
    fields = ("score", "comment", "created_at")
    ordering = ("-created_at",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin configuration for Genre model."""
    list_display = ("name", "movie_count")
    search_fields = ("name",)
    ordering = ("name",)

    @admin.display(description="Movies")
    def movie_count(self, obj):
        return obj.movies.count()


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Admin configuration for Person model."""
    list_display = ("full_name", "role", "photo_preview")
    list_filter = ("role",)
    search_fields = ("first_name", "last_name")
    ordering = ("last_name", "first_name")
    readonly_fields = ("photo_preview",)

    @admin.display(description="Name")
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    @admin.display(description="Photo")
    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" />', obj.photo.url)
        return "—"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Admin configuration for Movie model."""
    list_display = ("title", "release_year", "genre_list", "avg_rating", "created_at")
    list_filter = ("genres", "release_year")
    search_fields = ("title", "synopsis")
    ordering = ("-release_year", "title")
    readonly_fields = ("created_at", "updated_at")
    filter_horizontal = ("genres",)
    inlines = (RatingInline,)

    @admin.display(description="Genres")
    def genre_list(self, obj):
        return ", ".join(g.name for g in obj.genres.all())

    @admin.display(description="Avg Rating")
    def avg_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings:
            avg = sum(r.score for r in ratings) / len(ratings)
            return f"{avg:.1f}/10"
        return "—"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Admin configuration for Rating model."""
    list_display = ("movie", "score", "comment_short", "created_at")
    list_filter = ("score", "created_at")
    search_fields = ("movie__title", "comment")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    @admin.display(description="Comment")
    def comment_short(self, obj):
        return obj.comment[:50] + "..." if len(obj.comment) > 50 else obj.comment