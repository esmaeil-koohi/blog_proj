from django.shortcuts import render, get_object_or_404

from blog.models import Article


def post_detail(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, 'blog/article_details.html', {'article': article})
