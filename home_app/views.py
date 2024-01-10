from django.shortcuts import render
from blog.models import Article


def home(request):
    articles = Article.objects.all()
    print(articles.count())
    return render(request, 'home_app/index.html', {'article': articles})
