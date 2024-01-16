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
    path('messages/', views.MessageListView.as_view(), name='message_list'),
    path('message/edit/<int:pk>', views.MessageUpdateView.as_view(), name='message_edit'),
    path('message/delete/<int:pk>', views.DeleteView.as_view(), name='message_delete'),
    path('archive', views.ArchiveIndexArticleView.as_view(), name='archive'),
]
