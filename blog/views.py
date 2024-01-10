from django.shortcuts import render, get_object_or_404

from blog.models import Article


def post_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/article_details.html', {'article': article})


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/articles_list.html', {'articles': articles})
