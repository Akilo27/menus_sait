
from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog, name = 'blog'),
    path('create/', views.create_blog, name = 'create'),
    path('delete/<int:i>/', views.delete_blog, name='delete'),
]
