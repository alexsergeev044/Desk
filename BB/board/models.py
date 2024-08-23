from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    objects = None
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    CAT = (('news', 'новости'),
           ('sport', 'спорт'),
           ('Economy', 'экономика'),
           ('fashion', 'мода'),
           ('automotive_industry', 'автопром'),
           ('computer_games', 'компьютерные игры'),
           ('business', 'бизнес'),
           ('cooking', 'кулинария'),
           ('medicine', 'медицина'),
           ('путешествие', 'journey'))
    category = models.CharField(max_length=20, choices=CAT, verbose_name='Категория')
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, verbose_name='Название')
    text = RichTextField()


class Response (models.Model):
    objects = None
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)
