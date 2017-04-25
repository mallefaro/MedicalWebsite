from django.contrib import admin
from article.models import Article


class articleAdmin(admin.ModelAdmin):
    list_display = ('id', 'article_title', 'article_date')
    fields = ['article_title', 'article_text', 'article_date']
admin.site.register(Article, articleAdmin)
