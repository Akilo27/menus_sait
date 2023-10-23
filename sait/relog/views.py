from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Имя уже занято')
                return redirect('signup')
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Аккаунт создан успешно')
                return redirect('login')
        else:
            messages.error(request, 'неправильный пароль')
    else:
        return render(request, 'relog/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('login')
        else:
            return render(request, 'relog/login.html')


@login_required
def logout(request):
    auth_login(request)
    return redirect('login')


@login_required
def profile(request):
    return render(request, 'relog/profile.html')
