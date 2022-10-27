from django import forms
from .models import Reservation, Comments


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
                    'class': 'form-control', 'type': 'datetime-local'}),
        }

# Form to add comment


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comments
        fields = ['text', 'stars', 'image']

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'stars': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
