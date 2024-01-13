from django.shortcuts import render
from blog.models import Article
from django.core.paginator import Paginator


def home(request):
    articles = Article.objects.all()
    # recent_articles = Article.objects.all().order_by('-created')
    return render(request, 'home_app/index.html',{'article': articles})


# for test
def sidebar(request):
    data = {'name':'esmaeil'}
    return render(request, 'includes/sidebar.html', context=data)