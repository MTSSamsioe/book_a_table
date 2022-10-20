from django.shortcuts import render
from .models import Reservation

# Create your views here.

def home(request):
    return render(request, 'bookings/index.html')


def view_reservation(request):
    
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    navbar = {'navbar': 'view_reservation'}
    return render(request, 'bookings/my_bookings.html', context)
    

def menu(request):
    return render(request, 'bookings/menu.html')

def log(request):
    return render(request, 'bookings/log.html')