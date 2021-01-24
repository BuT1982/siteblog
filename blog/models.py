from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="Категория")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=150, verbose_name="Теги")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name="Теги")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")
    author = models.CharField(max_length=150, verbose_name="Автор")
    content = models.TextField(max_length=5000, verbose_name="Содержание", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name="Картинка", blank=True)
    views = models.IntegerField(default=0, verbose_name="Кол-во просмотров")
    category = models.ForeignKey(Category, max_length=150, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name="Теги")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
