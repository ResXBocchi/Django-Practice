from django.urls import include, path
from django.contrib import admin
from .views import Home


urlpatterns = [
    path('', Home.as_view())
]
