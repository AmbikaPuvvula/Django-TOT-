from django.shortcuts import render, redirect
from django.http import HttpResponse
from CrudApp.models import Student, StudentDetails
# Create your views here.


def addstudent(request):
    if request.method == 'POST':
        na = request.POST.get('name')
        roll = request.POST.get('rollno')
        age = request.POST.get('age')
        mnum = request.POST.get('mobile')
        em = request.POST.get('email')
        addr = request.POST.get('address')
        Student.objects.create(name=na, rollnum=roll,
                               age=age, mobile=mnum, email=em, address=addr)
        return redirect('read')

    return render(request, 'CrudApp/addstudent.html')


def read(request):
    datas = Student.objects.all()
    context = {'data': datas}
    return render(request, 'CrudApp/read.html', context)


def update(request, id):
    data = Student.objects.get(id=id)
    if request.method == 'POST':
        data.name = request.POST['name']
        data.rollnum = request.POST['rollno']
        data.age = request.POST['age']
        data.mobile = request.POST['mobile']
        data.email = request.POST['email']
        data.address = request.POST['address']
        data.save()
        return redirect('read')
    return render(request, 'CrudApp/update.html', {'data': data})


def delete(request, id):
    ob = Student.objects.get(id=id)
    if request.method == "POST":
        ob.delete()
        return redirect('read')
    return render(request, 'CrudApp/delete.html', {'info': ob})


def createstu(request):
    if request.method == 'POST':
        stname = request.POST.get('name')
        stnum = request.POST.get('snum')
        gen = request.POST.get('gender')
        lan = request.POST.getlist('lan')
        em = request.POST.get('email')
        br = request.POST.get('branch')
        dob = request.POST.get('dob')
        StudentDetails.objects.create(
            stuname=stname, stunum=stnum, email=em, lang=lan, branch=br, DOB=dob, gender=gen)
        return redirect('readstu')
    return render(request, 'CrudApp/cs.html')


def readstu(request):
    infos = StudentDetails.objects.all()
    context = {'info': infos}
    return render(request, 'CrudApp/r.html', context)


def updatestu(request, id):
    data = StudentDetails.objects.get(id=id)
    if request.method == 'POST':
        data.stuname = request.POST['name']
        data.stunum = request.POST['snum']
        data.gender = request.POST['gender']
        data.lang = request.POST['lan']
        data.email = request.POST['email']
        data.branch = request.POST['branch']
        data.DOB = request.POST['dob']
        data.save()
        return redirect('readstu')
    return render(request, 'CrudApp/u.html', {'data': data})


def deletestu(request, id):
    obj = StudentDetails.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('readstu')
    return render(request, 'CrudApp/d.html', {'info': obj})
