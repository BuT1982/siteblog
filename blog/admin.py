from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    """ Создаем автоматическое создания слага для постов"""
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'views')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'tags')


class CategoryAdmin(admin.ModelAdmin):
    """ Создаем автоматическое создания слага для категорий"""
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    """ Создаем автоматическое создания слага для тегов"""
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
