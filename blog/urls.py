from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('detail/<slug:slug>', views.post_detail, name='article_detail'),
    path('articlelsit', views.article_list, name='article_list'),

]