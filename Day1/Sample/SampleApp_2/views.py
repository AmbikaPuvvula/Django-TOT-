from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'SApp_2/home.html')


def bootstrap(request):
    return render(request, 'SApp_2/bstp.html')


def bst(request):
    return render(request, 'SApp_2/bst.html')
