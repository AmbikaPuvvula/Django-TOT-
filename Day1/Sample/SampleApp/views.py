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

def table(h,n):
    k = ""
    for i in range(1,11):
        k += " {} X {:02} = {:02}".format(n,i,n*i)+"<br>"
    #print(k)
    return HttpResponse(k)
    
def details(request,name,n):
    #print(name,n)
    return render(request,'SApp/details.html',{'na':name,'nu':n})

def samplecss(request):
    return render(request,'SApp/samplecss.html')

def login(request):
    return render(request,'SApp/login.html')

def register(request):
    return render(request,'SApp/register.html')

def samplejs(request):
    return render(request,'SApp/samplejs.html')

def jstask(request):
    return render(request,'SApp/jstask.html')