from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('detail/<slug:slug>', views.article_detail, name='article_detail'),
    path('articlelsit', views.article_list, name='article_list'),
    path('category/<int:pk>', views.category_detail, name="category_detail"),
    path('search/', views.search, name='search_articles'),
    path('contactus/', views.contactus, name='contact_us'),
]
