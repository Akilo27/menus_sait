from django.shortcuts import render
from .models import Blog
from django.http import HttpResponseRedirect
from menu.models import Menu




def blog(request):
    menus = Menu.objects.all().order_by('order')
    blogs = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blogs': blogs, 'menus': menus},)


def delete_blog(request, i):
    delete = Blog.objects.get(id=i)
    delete.delete()
    return HttpResponseRedirect('/blogs/')


def create_blog(request):
    menus = Menu.objects.all().order_by('order')
    if request.method == 'POST':
        username = request.POST.get('username')
        body = request.POST.get('body')
        Blog.objects.create(username=username, body=body)
        return HttpResponseRedirect('/blogs/')
    else:
        return render(request, 'blog/create.html', {'menus':menus})