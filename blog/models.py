from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ArticleManager(models.Manager):
     def counter(self):
        return len(self.all())

     def published(self):
        return self.filter(status=True)


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to="images/article")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # pub_date = models.DateTimeField(default=timezone.now())
    # pub_date = models.DateTimeField(default=timezone.datetime(day=20))
    status = models.BooleanField(default=True)
    objects = ArticleManager()

    def __str__(self):
        return f'{self.title} - {self.body[:30]}'
