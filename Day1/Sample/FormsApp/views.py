from django.shortcuts import render, redirect
from django.http import HttpResponse
from FormsApp.forms import DynamicFormCreation, Reg
from FormsApp.models import RegData, Register
# Create your views here.


def demo(request):
    return render(request, 'FormsApp/d.html')


def dhtml(request):
    fobj = DynamicFormCreation()
    if request.method == "POST":
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        age = request.POST.get('age')
        em = request.POST.get('email')
        psw = request.POST.get('password')
        url = request.POST.get('url')
        gen = request.POST.get('gender')
        br = request.POST.get('branch')
        lan = request.POST.getlist('languages')
        la = ""
        for l in lan:
            if lan.index(l) == 0:
                la += l
            else:
                la += ','+l
        # print('----------', la)
        RegData.objects.create(fname=fn, lname=ln, age=age, email=em,
                               password=psw, url=url, gender=gen, branch=br, lang=la)
        return redirect('read')
    return render(request, 'FormsApp/dhtml.html', {'form': fobj})


def read(request):
    datas = RegData.objects.all()
    context = {'data': datas}
    return render(request, 'FormsApp/details.html', context)


def userdata(request):
    fob = DynamicFormCreation()
    if request.method == "POST":
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        age = request.POST.get('age')
        em = request.POST.get('email')
        psw = request.POST.get('password')
        url = request.POST.get('url')
        gen = request.POST.get('gender')
        br = request.POST.get('branch')
        lan = request.POST.getlist('languages')
        la = ""
        for l in lan:
            if lan.index(l) == 0:
                la += l
            else:
                la += ','+l
        info = {'fname': fn, 'lname': ln, 'age': age, 'email': em,
                'password': psw, 'url': url, 'gender': gen, 'branch': br, 'language': la}
        return render(request, 'FormsApp/userdetails.html', {'info': info})
    return render(request, 'FormsApp/dhtml.html', {'form': fob})


def registerform(request):
    if request.method == "POST":
        # data = request.POST
        # print(data)
        # name = data['name']
        # print(name)
        f = RegisterForm(request.POST)
        f.save()
        return HttpResponse("Record Inserted using forms")
        #name = request.POST.get('name')
    f = RegisterForm()
    return render(request, 'FormsApp/regform.html', {'form': f})


def fetch(request):
    data = Register.objects.all()
    return render(request, 'FormsApp/display.html', {'data': data})


def home(request):
    return render(request, 'FormsApp/home.html')


def reg(request):
    if request.method == "POST":
        fd = Reg(request.POST)
        if fd.is_valid():
            fd.save()
            # print(fd)
            return redirect("/form")
    fd = Reg()
    return render(request, 'FormsApp/register.html', {'data': fd})


def details(request):
    data = Register.objects.all()
    return render(request, 'FormsApp/data.html', {'data': data})


def update(request, id):
    a = Register.objects.get(id=id)
    if request.method == "POST":
        u = Reg(request.POST, instance=a)
        if u.is_valid():
            u.save()
            return redirect('/form/details')
    u = Reg(instance=a)
    return render(request, 'FormsApp/update.html', {'u': u})


def delete(request, id):
    d = Register.objects.get(id=id)
    if request.method == "POST":
        d.delete()
        return redirect('/form/details')
    return render(request, 'FormsApp/delete.html', {'info': d})
