from django.shortcuts import render

def homepage(request):
    return render(request,'shop/home.html')

def loginuser(request):
    return render(request,'users/login.html')

def logoutuser(request):
    return render(request,'users/logout.html')