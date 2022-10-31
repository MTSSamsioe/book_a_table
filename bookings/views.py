from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse , Http404
import os
from .models import Reservation, Comments
from .forms import ReservationForm, CommentForm
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
import math
# Create your views here.


def home(request):

    form = CommentForm()
    comments = Comments.objects.filter(approved=1)
    context = {
        'form': form,
        'comments': comments,
    }
    return render(request, 'bookings/index.html', context)


def view_reservation(request):
    
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(status=1, user=request.user)
        form = ReservationForm()
        context = {
            'reservations': reservations,
            'form': form,
            
        }
        return render(request, 'bookings/my_bookings.html', context)
    else:
        return render(request, 'bookings/my_bookings.html')

def add_reservation(request):
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            
            creator = form.save(commit=False)
            creator.user = request.user
            creator.save()
            messages.success(request,
                             'Your reservation was saved and is awaiting approval from resturant')
            return redirect('/my_bookings/')
        else:
            
            reservations = Reservation.objects.filter(
                status=1, user=request.user)
            context = {
                'form': form, 'reservations': reservations, 
                
            }
            messages.error(request, 'Something went wrong please press "Create button" again')
            return   render(request, 'bookings/my_bookings.html', context)
        
            # return redirect('/my_bookings/', )
    form = ReservationForm()
    context = {
        'form': form
    }

    return render(request, 'bookings/my_bookings.html', context)


def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your reservation was updated successfully')
            return redirect('/my_bookings/')
        else:
            messages.error(request, 'Something went wrong! Please try again')
    form = ReservationForm(instance=reservation)
    context = {
        'form': form
    }
    return render(request, 'bookings/edit.html', context)


def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.delete()
    messages.success(request, 'Your reservation was deleted successfully')
    return redirect('/my_bookings/')

def menu(request):
    try:
        return FileResponse(open('bookings/static/images/menu_fuzzy.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
#def menu(request):
#    menu = os.path.join('bookings/static/images/', 'menu_fuzzy.pdf')
#    return FileResponse(open(menu, 'rb'), content_type= 'appliccation/pdf')

def add_comment(request):

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # associate user with istance
            creator = form.save(commit=False)
            creator.user = request.user
            creator.save()
            messages.success(request, 'Your comment has been saved and waiting approval')
            return redirect('/')
            # print(form.cleaned_data)
        else:
            # ta bort eventuellt
            messages.error(request, 'Something went wrong! Please try again')

    form = CommentForm()
    context = {
        'form': form
    }
    return render(request, 'bookings/index.html', context)
