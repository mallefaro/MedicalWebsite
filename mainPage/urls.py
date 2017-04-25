
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^articles/(?P<article_id>[0-9]+)/$', views.show_articles, name="article"),
    url(r'^$', views.mainPage, name="mainPage"),
]
