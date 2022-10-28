from django import forms
from .models import Reservation, Comments
import datetime
from django.utils import timezone
from django.contrib import messages
import math


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
            'date_time': forms.DateTimeInput(format='%d/%m/%Y %H:%M', attrs={
                    'class': 'form-control', 'type': 'datetime-local',
                    'id': 'date_time_input'}),
        }

    def clean_number_of_guests(self, *args, **kwargs):
        total_tables_for_two = 2
        date_time = self.cleaned_data.get('date_time')
        number_of_guests = self.cleaned_data.get('number_of_guests')
        #tables_needed = math.ceil(number_of_guests / 2)
        if number_of_guests > total_tables_for_two:
            raise forms.ValidationError('There are no tables ')
        else:
            return number_of_guests

    def clean_date_time(self, *args, **kwargs):
        date_time = self.cleaned_data.get('date_time')
        if date_time > timezone.now():
            return date_time
        else:
            raise forms.ValidationError('Reservation can not be before todays date and time')

        
        # total_tables_for_two = 6
        # number_of_guests = self.cleaned_data.get('numbers_of_guests')
        # tables_needed = math.ceil(number_of_guests / 2)
        # table_collide = Reservation.objects.filter(Reservation.objects.filter(date_time__gte=date_time and Reservation.objects.filter(date_time__lte=date_time_end)


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comments
        fields = ['text', 'stars', 'image']

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'stars': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})}
