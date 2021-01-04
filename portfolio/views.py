from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from datetime import datetime
from .models import ArticleModel
from django.utils import timezone
from .forms import ArticleForm

# Create your views here.

# Function based view
# def home(request):
#     if request.method == 'GET':
#         return HttpResponse("Welcome to my portfolio")
#
# Class based view


class Home(View):

    def get(self, request):
        return HttpResponse('Welcome to my portfolio!')

    def post(self, request):
        return HttpResponse('What are you trying to post?')


class Article(View):

    def get(self, request):
        articles = ArticleModel.objects.all()

        return render(request, "articles.html", {"articles": articles, "form": ArticleForm()})

    def post(self, request):
        title = request.POST['title']
        category = request.POST['category']
        author = request.POST['author']
        content = request.POST['content']
        dt = datetime.now(timezone.utc)

        ArticleModel.objects.create(title=title,
                                    category=category,
                                    author=author,
                                    content=content,
                                    created_at=dt)

        return redirect('/portfolio/articles')


class ArticleDetails(View):
    def get(self, request, id):
        try:
            article = ArticleModel.objects.get(id=id)
            return render(request, "article_details.html", {"article": article})
        except ArticleModel.DoesNotExist:
            return HttpResponseNotFound()

