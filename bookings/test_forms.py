from django.test import TestCase
from .forms import CommentForm, ReservationForm

# Create your tests here.
class TestCommentForm(TestCase):
    
    def test_text_is_required(self):
        form = CommentForm({'text': ''})
        self.assertFalse(form.is_valid())
       # self.assertIn('text', form.errors.keys())
       # self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_stars_is_required(self):
        form = CommentForm({'text': 'Test text', 'stars': '2'})
        self.assertTrue(form.is_valid())

    def test_image_is_not_required(self):
        form = CommentForm({'text': 'Test text', 'stars': '2'})
        self.assertTrue(form.is_valid())
    
    def test_fields_exisists_in_meta_class(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ['text', 'stars', 'image'])

# Test for Reservation form

class TestReservationForm(TestCase):
    # Test for field first_name
    def test_first_name_is_required(self):
        form = ReservationForm({'first_name': ''})
        self.assertFalse(form.is_valid())
       
    
    # Test for field last_name

    def test_last_name_is_required(self):
        form = ReservationForm({'last_name': 'dfg'})
        self.assertFalse(form.is_valid())
       

    # Test for field email

    def test_email_is_required(self):
        form = ReservationForm({'email': ''})
        self.assertFalse(form.is_valid())
    

    # Test for field date_time

    def test_date_time_is_required(self):
        form = ReservationForm({'date_time': '2002'})
        self.assertFalse(form.is_valid())

     # Test for field number of guests  
    def test_number_of_guests_is_required(self):
        form = ReservationForm({'number_of_guests': ''})
        self.assertFalse(form.is_valid())
    