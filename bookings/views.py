from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

# Create your views here.

def home(request):
    return render(request, 'bookings/index.html')


def view_reservation(request):
    
    reservations = Reservation.objects.filter(status= 1)
    form = ReservationForm()
    
    context = {
        'reservations': reservations,
        'form': form
    }
    
    return render(request, 'bookings/my_bookings.html', context)

def add_reservation(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        number_of_guests = request.POST.get('number_of_guests')
        Reservation.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            date = date,
            number_of_guests = number_of_guests
            )
        return redirect('/my_bookings/')
    form = ReservationForm()
    context = {'form': form}

    return render(request, 'bookings/my_bookings.html', context)


def menu(request):
    return render(request, 'bookings/menu.html')

def log(request):
    return render(request, 'bookings/log.html')