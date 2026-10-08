from django.db import models
from django.utils import timezone


class Author(models.Model):
    """
    Author model representing a news article author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="authors/", blank=True, null=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    """
    Category model for organizing articles into topics.
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    Article model representing a news article.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.TextField()
    body = models.TextField()
    featured_image = models.ImageField(upload_to="articles/", blank=True, null=True)
    published_at = models.DateTimeField(default=timezone.now)

    # ForeignKey to Author with PROTECT on_delete
    # JUSTIFICATION: PROTECT prevents deletion of an Author who has published articles.
    # This ensures referential integrity - we don't want orphaned articles without an author.
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name="articles"
    )

    # ManyToManyField to Category
    # JUSTIFICATION: An article can belong to multiple categories, and a category
    # can contain multiple articles. This many-to-many relationship models this
    # bidirectional association correctly.
    categories = models.ManyToManyField(
        Category,
        related_name="articles",
        blank=True
    )

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title