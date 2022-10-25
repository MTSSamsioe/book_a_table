"""django_bookings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookings.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('add_comment', add_comment, name = 'add_comment'),
    path('my_bookings/', view_reservation, name = 'view_reservation'),
    path('menu/', menu, name = 'menu'),
    path('log/', log, name = 'log'),
    path('my_bookings/add', add_reservation, name = 'add'),
    path('edit/<reservation_id>', edit_reservation, name = 'edit'),
    path('delete/<reservation_id>', delete_reservation, name = 'delete'),
    path('accounts/', include('allauth.urls')),
    
]
