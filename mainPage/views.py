from django.shortcuts import render, get_object_or_404

from article.models import Article


def mainPage(request):
    articles = Article.objects.order_by("-id")[0:9]
    return render(request, 'main/index.html', {'articles': articles})

def show_articles(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'main/article.html', {'article': article})

