from django.urls import path
from . import views

urlpatterns = [
    path('', views.relog, name='relog'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<str:name>/', views.profile, name='profile'),
]