from django import forms
from .models import Reservation, Comments
import datetime
from django.utils import timezone
from django.contrib import messages
from django.core.validators import MinValueValidator
import math

# Section for reservations form

# Code on how to style widgets are from:
# https://www.youtube.com/watch?v=6-XXvUENY_8


class ReservationForm(forms.ModelForm):

    class Meta:

        model = Reservation
        fields = ['first_name', 'last_name', 'email',
                  'number_of_guests', 'date_time']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'number_of_guests': forms.Select(attrs={'class': 'form-select'}),
            'date_time': forms.DateTimeInput(attrs={
                    'class': 'form-control', 'type': 'datetime-local'}),
        }
        labels = {
                'first_name': 'First Name',
                'last_name': 'Last Name',
                'email': 'E-mail',
                'number_of_guests': 'Number Of Guests',
                'date_time': 'Date & Time Opening Hours: 11.00 - 22.30',
        }
# Section for comments form


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comments
        fields = ['text', 'stars', 'image']

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'stars': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})}

        labels = {
            'text': 'Write Your Comment Here',
            'stars': 'Stars 1 - 5',
            'image': 'Upload Image (Optional)',
        }
