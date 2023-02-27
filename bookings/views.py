from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404, HttpResponse
import os
from .models import Reservation, Comments
from .forms import ReservationForm, CommentForm
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
import math

# View for rendering index.html with form and comments


def home(request):
    """View for rendering index.html"""
    form = CommentForm()
    comments = Comments.objects.filter(approved=1)
    context = {
        'form': form,
        'comments': comments,
    }
    return render(request, 'bookings/index.html', context)

# View for rendering my_bookings.html with form and reservation


def view_reservation(request):
    """View for viewing reservations"""

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

# View for add a resrevation


def add_reservation(request):
    """ View for adding a reservation """

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():

            creator = form.save(commit=False)
            creator.user = request.user
            creator.save()
            messages.success(request,
                             '''Your
                             reservation was saved and is
                             awaiting approval from resturant''')
            return redirect('/my_bookings/')
        else:

            reservations = Reservation.objects.filter(
                status=1, user=request.user)
            context = {
                'form': form, 'reservations': reservations,

            }
            messages.error(request, '''Something went wrong
                           please press "Create button" again''')
            return render(request, 'bookings/my_bookings.html', context)

            # return redirect('/my_bookings/', )
    form = ReservationForm()
    context = {
        'form': form
    }

    return render(request, 'bookings/my_bookings.html', context)

# View for editing a resrevation


def edit_reservation(request, reservation_id):
    """View for editing reservations"""

    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your reservation was updated successfully')
            return redirect('/my_bookings/')
        else:
            messages.error(request, '''Something went wrong! Please try again
                                       Possible errors:
                                       - Date and time is before present time
                                       - Time is outside opening hours
                                       - There are no availeble tables''')
    form = ReservationForm(instance=reservation)
    context = {
        'form': form,
        'reservation': reservation,
    }
    return render(request, 'bookings/edit.html', context)

# View for deleting a resrevation


def delete_reservation(request, reservation_id):
    """View for deleting reservations """

    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.delete()
    messages.success(request, 'Your reservation was deleted successfully')
    return redirect('/my_bookings/')

# View for rendering a pdf file with a menu

# Code in menu function was taken from
# https://www.codespeedy.com/show-a-pdf-file-in-django-instead-of-downloading/


def menu(request):
    """View for showing the resturants menu """

    try:
        with open('bookings/static/bookings/images/menu_fuzzy.pdf', 'rb') \
                as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=menu_fuzzy.pdf'
        return response
    except FileNotFoundError:
        raise Http404()

# View for adding a review comment


def add_comment(request):
    """View for adding a comment"""

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # associate user with istance
            creator = form.save(commit=False)
            creator.user = request.user
            creator.save()
            messages.success(request, '''Your comment
                             has been saved and waiting approval''')
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

# View for page not found


def page_not_found(request, exception):
    """View for handeling page not found"""

    return render(request, 'bookings/page_not_found.html')

# View for server error


def server_error(request):
    """View for handeling server error"""

    return render(request, 'bookings/server_error.html')
