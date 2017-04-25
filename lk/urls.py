
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^registration/?', views.registration, name="registration"),
    url(r'^account/', views.auth, name='profile'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^', views.lk, name="lk"),

]
