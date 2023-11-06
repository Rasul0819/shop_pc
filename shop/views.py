from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .models import User
from .forms import UserCreationFormByMe
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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

# def register(request):
#     forms = UserCreationFormByMe()
#     context = {
#         'forms':forms,
#         'error':'fill the all field please'
#     }
#     print(forms)
#     return render(request,'users/register.html',context)


def register(request):
    if request.method == 'GET':
        form  = UserCreationFormByMe()
        context = {'form': form}
        return render(request, 'users/register.html', context)
    if request.method == 'POST':
        form  = UserCreationFormByMe(request.POST)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account was created for ' + user)
        return redirect('homepage')
    else:
        print('Form is not valid')
        messages.error(request, 'Error Processing Your Request')
        context = {'form': form}
        return render(request, 'users/register.html', context)
    return render(request, 'users/register.html', {})