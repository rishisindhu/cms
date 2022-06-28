from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login_view(request):
    if (request.method =='POST'):


        uname =request.POST.get('uname')
        password =request.POST.get('psw')
        print("password>>>>>>",password)
        print("uname>>>>>",uname)
    return render(request,'login.html')


def home_view(request) :
    return render(request,'home.html' )   