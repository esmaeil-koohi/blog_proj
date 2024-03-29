# Generated by Django 5.0.1 on 2024-01-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, default=1, unique=True),
            preserve_default=False,
        ),
    ]
