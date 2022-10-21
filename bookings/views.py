from django.shortcuts import render, redirect, get_object_or_404
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
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/my_bookings/')
    form = ReservationForm()
    context = {
        'form': form
    }

    return render(request, 'bookings/my_bookings.html', context)

def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id = reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance = reservation)
        if form.is_valid():
            form.save()
            return redirect('/my_bookings/')
    
    form = ReservationForm(instance = reservation)
    context = {
        
        'form': form
    }
    return render(request, 'bookings/edit.html', context)

def menu(request):
    return render(request, 'bookings/menu.html')

def log(request):
    return render(request, 'bookings/log.html')