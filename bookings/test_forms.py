from django.test import TestCase
from django.contrib.auth.models import User
from .forms import CommentForm, ReservationForm
from .models import Reservation, Comments

# Set up class


class Setup_Class(TestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'test'
        test_user = User.objects.create_user(username=self.username,
                                             email='test@test.com',
                                             password=self.password)


class TestCommentForm(Setup_Class):

    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)

    def test_text_is_required(self):
        form = CommentForm({'text': '', 'stars': 3})
        self.assertFalse(form.is_valid())

    def test_stars_is_required(self):
        form = CommentForm({'text': 'Test text', 'stars': ''})
        self.assertFalse(form.is_valid())

    def test_image_is_not_required(self):
        form = CommentForm({'text': 'Test text', 'stars': '2'})
        self.assertTrue(form.is_valid())

    def test_fields_exisists_in_meta_class(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ['text', 'stars', 'image'])

# Test for Reservation form


class TestReservationForm(Setup_Class):

    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.reservation = \
            Reservation.objects.create(
                                       first_name='first',
                                       last_name='last',
                                       email='email@emial.com',
                                       date_time='2002-11-15 15:00',
                                       date_time_end='2002-11-15 17:00',
                                       number_of_guests=2)

    # Test for field first_name

    def test_first_name_is_required(self):
        form = ReservationForm({})
        self.assertFalse(form.is_valid())

    # Test for field last_name

    # def test_last_name_is_required(self):˜˜
    #     form = ReservationForm({'last_name': 'dfg'})
    #     self.assertFalse(form.is_valid())

    # Test for field email

    # def test_email_is_required(self):
    #     form = ReservationForm({'email': ''})
    #     self.assertFalse(form.is_valid())

    # Test for field date_time

    # def test_date_time_is_required(self):
    #     form = ReservationForm({'date_time': '2002'})
    #     self.assertFalse(form.is_valid())

    # Test for field number of guests
    # def test_number_of_guests_is_required(self):
    #     form = ReservationForm({'number_of_guests': ''})
    #     self.assertFalse(form.is_valid())
