from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category, Comment
from django.core.paginator import Paginator
from . forms import ContactUsForm


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    if request.POST:
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
    return render(request, 'blog/article_details.html', {'article': article})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', {'articles': objects_list})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, "blog/articles_list.html", {'articles': articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request, "blog/articles_list.html", {'articles':objects_list})


def contactus(request):
    form = ContactUsForm()
    return render(request, "blog/contact_us.html", {'form':form})