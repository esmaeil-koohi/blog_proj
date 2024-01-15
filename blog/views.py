from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Category, Comment, Message
from django.core.paginator import Paginator
from .forms import ContactUsForm, MessageForms
from django.views.generic.base import View, TemplateView
from django.views.generic import ListView, DetailView, FormView
from django.urls import reverse_lazy


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    if request.POST:
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
    return render(request, 'blog/article_detail.html', {'article': article})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', {'articles': objects_list})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, "blog/article_list.html", {'articles': articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request, "blog/article_list.html", {'articles': objects_list})


def contactus(request):
    if request.method == 'POST':
        form = MessageForms(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            Message.objects.create(title=title, text=text, email=email)
             # instance = form.save(commit=True)
    else:
        form = MessageForms()
    return render(request, "blog/contact_us.html", {'form': form})


class ArticleList(TemplateView):
    template_name = "blog/article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 1


class ArticleDetailView(DetailView):
    model = Article


class ContactUsView(FormView):
    template_name = "blog/contact_us.html"
    form_class = MessageForms
    success_url = reverse_lazy('home:main')

    def form_valid(self, form):
        form_data = form.cleaned_data
        Message.objects.create(**form_data)
        return super().form_valid(form)

