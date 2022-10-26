from django import forms
from .models import Reservation, Comments



class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.DateInput):
    input_type = 'time'

class ReservationForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'email', 'date', 'time', 'number_of_guests']

        widgets = {
            'first_name': forms.TextInput(attrs= {'class': 'form-control'}),
            'last_name': forms.TextInput(attrs= {'class': 'form-control'}),
            'email': forms.EmailInput(attrs= {'class': 'form-control'}),
            'date': DateInput(attrs= {'class': 'form-control'}),
            'time': TimeInput(format='%H:%M', attrs={'class': 'form-control'}),
            'number_of_guests': forms.NumberInput(attrs= {'class': 'form-control'})
        }

# Form to add comment


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ['text','stars', 'image']

        widgets = {
            'text': forms.Textarea(attrs= {'class': 'form-control'}),
            'stars': forms.Select(attrs= {'class': 'form-select'}),
            'image': forms.FileInput(attrs= {'class': 'form-control'}),
            
            
        }