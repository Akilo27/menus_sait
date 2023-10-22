
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blog.urls')),
    path('news/', include('news.urls')),
    path('main/', include('menu.urls')),
    path('', include('menu.urls')),
    path('polls/', include('polls.urls'))
]
