from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Welcome Message')

def about(s):
    return HttpResponse("<h2 style='background-color:skyblue;color:white;padding:3px;margin-left:230px;margin-right:230px'>About page..</h2>")

def mesg(m,name):
    return HttpResponse("<h2>Hii... {} welcome</h2>".format(name))

def data(n,name,num):
    return HttpResponse("<h2>Hi.. {} your number is {}</h2>".format(name,num))