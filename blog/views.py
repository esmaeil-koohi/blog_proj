from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category
from django.core.paginator import Paginator

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/article_details.html', {'article': article})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    print(page_number)
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', {'articles': objects_list})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, "blog/articles_list.html", {'articles': articles})

