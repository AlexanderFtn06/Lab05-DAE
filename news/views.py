from django.shortcuts import render
from .models import Article, Category


def home(request):
    """
    Home page view displaying the latest articles.
    """
    articles = Article.objects.select_related("author").prefetch_related("categories")
    categories = Category.objects.all()
    latest_article = articles.first()

    context = {
        "articles": articles,
        "categories": categories,
        "latest_article": latest_article,
    }
    return render(request, "news/home.html", context)