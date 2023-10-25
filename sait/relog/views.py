from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from menu.models import Menu

def relog(request):
    menus = Menu.objects.all().order_by('order')
    return render(request, 'relog/relog.html', {'menus': menus})


def signup(request):
    menus = Menu.objects.all().order_by('order')


    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('signup')
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'relog/signup.html',{'menus':menus})


def login(request):
    menus = Menu.objects.all().order_by('order')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(f'/relog/profile/{username}/', username=username)
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'relog/login.html', {'menus': menus})


@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required
def profile(request, username):
    username = User.objects.get(username=username)
    menus = Menu.objects.all().order_by('order')
    return render(request, 'relog/profile.html', {'user': username, 'menus': menus})
