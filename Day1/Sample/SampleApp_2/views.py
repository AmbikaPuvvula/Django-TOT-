from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'SApp_2/home.html')


def bootstrap(request):
    return render(request, 'SApp_2/bstp.html')


def bst(request):
    return render(request, 'SApp_2/bst.html')


def login(request):
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pswd']
        #print(u, p)
        # return HttpResponse("Hii.. your username is: {}".format(u))
        if u == 'Ambika' and p == 'Ambika123':
            return HttpResponse("<h2> Hiii.. Welcome {} </h2>" .format(u))
        else:
            return HttpResponse('<h2>Invalid....)</h2>')
        # return render(request, 'SApp_2/details.html', {'us': u, 'ps': p})
    return render(request, 'SApp_2/login.html')


def reg(request):
    if request.method == "POST":
        un = request.POST['uname']
        em = request.POST['email']
        ps = request.POST['pswd']
        cps = request.POST['cpswd']
        gn = request.POST['optradio']
        da = request.POST['dob']
        c = request.POST['course']
        ln = request.POST.getlist('lan')
        r = request.POST['range']
        f = request.POST['file']
        cm = request.POST['txt']
        #print(un, em, ps, cps, gn, da, ln, c, r, f, cm)
        return render(request, 'SApp_2/regdetails.html', {'username': un, 'email': em, 'password': ps, 'cpassword': cps, 'gender': gn, 'dateofbirth': da, 'cou': c, 'language': ln, 'ran': r, 'fileupload': f, 'comments': cm})
    return render(request, 'SApp_2/register.html')
