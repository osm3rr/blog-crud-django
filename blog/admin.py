from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at', 'author__username')

# Register your models here.
admin.site.register(Article, ArticleAdmin)