from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .models import User
def homepage(request):
    return render(request,'shop/home.html')

def loginuser(request):
    # return render(request,'users/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            # Обработка неправильных учетных данных
            return render(request, 'users/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'users/login.html')

def logoutuser(request):
    logout(request)
    return redirect('homepage')

