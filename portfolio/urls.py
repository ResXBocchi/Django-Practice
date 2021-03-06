from django.urls import include, path
from django.contrib import admin
from .views import Home, Article, ArticleDetails


urlpatterns = [
    path('', Home.as_view()),
    path('articles', Article.as_view()),
    path('articles/<int:id>', ArticleDetails.as_view())
]
