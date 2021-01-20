from django.shortcuts import render, redirect
from .forms import UserReg, UpdateProfile, UpdateUserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from RoleApp.models import Update
# Create your views here.


def home(request):
    return render(request, 'RoleApp/home.html')


def about(request):
    return render(request, 'RoleApp/about.html')


def contactus(request):
    return render(request, 'RoleApp/contactus.html')


def register(request):
    if request.method == "POST":
        data = UserReg(request.POST)
        if data.is_valid():
            data.save()
            messages.success(
                request, "hii you are successfully registered")
            return redirect('login')
    formfields = UserReg()
    return render(request, 'RoleApp/register.html', {'formfields': formfields})


@login_required
def dashboard(request):
    return render(request, 'RoleApp/dashboard.html')


@login_required
def profile(request):
    return render(request, 'RoleApp/profile.html')


@login_required
def updateprofile(request):
    if request.method == 'POST':
        data = UpdateProfile(request.POST, instance=request.user)
        udata = UpdateUserProfile(request.POST, request.FILES,
                                  instance=request.user.update)
        if data.is_valid() and udata.is_valid():
            data.save()
            udata.save()
            messages.success(request, "Updated Successfully")
            return redirect('/profile')
    data = UpdateProfile(instance=request.user)
    udata = UpdateUserProfile(instance=request.user.update)
    return render(request, 'RoleApp/updateprofile.html', {'data': data, 'udata': udata})
