from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html

from .models import Author, Category, Article


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Author model.
    """
    list_display = ["full_name", "articles_count"]
    search_fields = ["first_name", "last_name"]
    list_select_related = []

    @admin.display(description="Nombre completo", ordering="last_name")
    def full_name(self, obj):
        """Return the author's full name."""
        return f"{obj.first_name} {obj.last_name}"

    @admin.display(description="Noticias")
    def articles_count(self, obj):
        """Return the number of articles written by this author."""
        # Using the related_name 'articles' from the ForeignKey in Article model
        return obj.articles.count()

    def get_queryset(self, request):
        """Annotate queryset with article count for efficient display."""
        qs = super().get_queryset(request)
        return qs.annotate(articles_count=Count("articles"))


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Category model.
    """
    list_display = ["name", "slug", "articles_count"]
    search_fields = ["name", "description"]
    prepopulated_fields = {"slug": ("name",)}

    @admin.display(description="Noticias")
    def articles_count(self, obj):
        """Return the number of articles in this category."""
        return obj.articles.count()

    def get_queryset(self, request):
        """Annotate queryset with article count for efficient display."""
        qs = super().get_queryset(request)
        return qs.annotate(articles_count=Count("articles"))


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Article model.
    """
    list_display = ["title", "author", "published_at", "categories_display"]
    list_filter = ["author", "categories", "published_at"]
    search_fields = ["title", "summary", "body"]
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ["categories"]
    date_hierarchy = "published_at"
    list_select_related = ["author"]

    @admin.display(description="Categorías")
    def categories_display(self, obj):
        """Return a comma-separated list of category names."""
        return ", ".join([category.name for category in obj.categories.all()])