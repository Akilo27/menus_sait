from django.shortcuts import render
from .models import Menu

def main(request):
    menus = Menu.objects.all().order_by('order')
    return render(request, 'main.html',{'menus': menus})
