from django.shortcuts import render
from .models import Reservation

# Create your views here.

def say_hello(request):
    return render(request, 'bookings/index.html')


def view_reservation(request):
    
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'bookings/my_bookings.html', context)
