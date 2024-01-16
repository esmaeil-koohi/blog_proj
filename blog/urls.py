from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('detail/<slug:slug>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('articlelsit', views.ArticleListView.as_view(), name='article_list'),
    path('category/<int:pk>', views.category_detail, name="category_detail"),
    path('search/', views.search, name='search_articles'),
    # path('contactus/', views.ContactUsView.as_view(), name='contact_us'),
    path('contactus/', views.MessageView.as_view(), name='contact_us'),
]
