from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


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
    category = models.ManyToManyField(Category, related_name="articles")
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to="images/article")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, unique=True)
    objects = ArticleManager()

    # pub_date = models.DateTimeField(default=timezone.now())
    # pub_date = models.DateTimeField(default=timezone.datetime(day=20))

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        # return reverse('blog:article_detail', args=[self.id])
        return reverse('blog:article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title} - {self.body[:30]}'

    class Meta:
        ordering = ("-created",)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]


class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


