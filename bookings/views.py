from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Reservation, Comments
from .forms import ReservationForm , CommentForm
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    form = CommentForm()
    comments = Comments.objects.filter(approved = 1)
    context = {
        'form': form,
        'comments': comments,
    }
    return render(request, 'bookings/index.html', context)


def view_reservation(request):
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(status= 1, user = request.user)
        form = ReservationForm()
        
        context = {
            'reservations': reservations,
            'form': form
        }
        
        return render(request, 'bookings/my_bookings.html', context)
    else:
        return render(request, 'bookings/my_bookings.html')

def check(request):
    return JsonResponse({'availeble': True})

def add_reservation(request):
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # associate user with istance 
            creator = form.save(commit=False)
            creator.user = request.user 
            creator.save()
            messages.success(request, 'Your reservation was created successfully')
            return redirect('/my_bookings/')
        else:
            messages.error(request, 'Something went wrong! Please try again')
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
            messages.success(request, 'Your reservation was updated successfully')
            return redirect('/my_bookings/')
        else:
            messages.error(request, 'Something went wrong! Please try again')
    form = ReservationForm(instance = reservation)
    context = {
        
        'form': form
    }
    return render(request, 'bookings/edit.html', context)

def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id = reservation_id)
    reservation.delete()
    messages.success(request, 'Your reservation was deleted successfully')
    return redirect('/my_bookings/')


def menu(request):
    return render(request, 'bookings/menu.html')

def log(request):
    return render(request, 'bookings/log.html')


# comments

def add_comment(request):    
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # associate user with istance 
            creator = form.save(commit=False)
            creator.user = request.user 
            creator.save()
            messages.success(request, 'Your comment has been saved')
            return redirect('/')
            #print(form.cleaned_data)
        else:
            # ta bort eventuellt
            messages.error(request, 'Something went wrong! Please try again')
            
    form = CommentForm()
    context = {
        'form': form
    }
    return render(request, 'bookings/index.html', context)