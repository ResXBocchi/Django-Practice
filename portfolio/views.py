from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from datetime import datetime

# Create your views here.

# Function based view
# def home(request):
#     if request.method == 'GET':
#         return HttpResponse("Welcome to my blog")
#
# Class based view
class Home(View):

    def get(self, request):
        return HttpResponse('Welcome to my portfolio!')

    def post(self, request):
        return HttpResponse('What are you trying to post?')

class Article(View):

    def get(self, request):
        articles = [
            {
                "title": "Title",
                "category": "Test",
                "author": "Myself",
                "content": "Just some lorem ipsum content",
                "creation_date": datetime.now()
            },
            {
                "title": "Title2",
                "category": "Test2",
                "author": "Myself",
                "content": "Just some lorem ipsum content 2",
                "creation_date": datetime.now()
            }
        ]
        return render(request,'articles.html', {"articles":articles})