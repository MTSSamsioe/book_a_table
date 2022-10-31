from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from bookings.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add_comment', add_comment, name='add_comment'),
    path('my_bookings/', view_reservation, name='view_reservation'),
    path('menu/', menu, name='menu'),
    path('my_bookings/add', add_reservation, name='add'),
    path('edit/<reservation_id>', edit_reservation, name='edit'),
    path('delete/<reservation_id>', delete_reservation, name='delete'),
    path('accounts/', include('allauth.urls')),
    

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),