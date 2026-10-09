from django.shortcuts import render, get_object_or_404
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


def article_detail(request, slug):
    """
    Article detail view displaying a single article with all its content.
    """
    article = get_object_or_404(
        Article.objects.select_related("author").prefetch_related("categories"),
        slug=slug,
    )
    categories = Category.objects.all()

    context = {
        "article": article,
        "categories": categories,
    }
    return render(request, "news/article_detail.html", context)