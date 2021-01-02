from django.urls import include, path
from django.contrib import admin
from .views import Home, Article


urlpatterns = [
    path('', Home.as_view()),
    path('articles', Article.as_view())
]
