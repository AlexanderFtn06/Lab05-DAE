from django.shortcuts import render
from django.utils import timezone
from .models import Article, Category


def home(request):
    """
    Home page view displaying the latest articles.
    """
    articles = Article.objects.select_related("author").prefetch_related("categories").filter(
        published_at__lte=timezone.now()
    )
    categories = Category.objects.all()
    latest_article = articles.first()

    context = {
        "articles": articles,
        "categories": categories,
        "latest_article": latest_article,
    }
    return render(request, "news/home.html", context)