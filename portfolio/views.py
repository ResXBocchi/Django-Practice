from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
#Create your views here.

# Function based view
# def home(request):
#     if request.method == 'GET':
#         return HttpResponse("Welcome to my blog")
#
# Class based view
class Home(View):
    def get(self,request):
        return HttpResponse('Welcome to my portfolio!')
    def post(self,request):
        return HttpResponse('What are you trying to post?')