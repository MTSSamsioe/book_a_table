from django.contrib.auth.models import User
from django.test import TestCase
from .models import Reservation, Comments
from django.test import client


class Setup_Class(TestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'test'
        test_user = User.objects.\
            create_user(username=self.username,
                        email='test@test.com', password=self.password)

# Section for editing reviews


class Testviews_req_log_in(Setup_Class):

    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)

    def test_edit_reservation(self):

        reservation = Reservation.objects.create(
                                                 first_name='first',
                                                 last_name='last',
                                                 email='email@emial.com',
                                                 date_time='2022-11-15 15:00',
                                                 date_time_end='''2022-11-
                                                 15 17:00''',
                                                 number_of_guests=2)
        response = self.client.get(f'/edit/{reservation.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/edit.html')

# Section for testing error response for reviews

    def test_respons_ok_on_submit(self):

        response = self.client.post('/my_bookings/add', {
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@emial.com',
            'date_time': '2002-11-15 15:00',
            'number_of_guests': 2,
            })
        self.assertEqual(response.status_code, 200)

# Section for testing deleting reviews

    def test_can_delete_reservation(self):
        reservation = Reservation.objects.create(
                                                 first_name='first',
                                                 last_name='last',
                                                 email='email@emial.com',
                                                 date_time='2022-11-25 15:00',
                                                 date_time_end='''2022-
                                                 11-25 17:00''',
                                                 number_of_guests=2)
        response = self.client.get(f'delete/{reservation.id}')

    def test_add_comment(self):

        response = self.client.post('/add_comment', {'text': 'Test',
                                                     'stars': '3'})
        self.assertEqual(Comments.objects.count(), 1)
        self.assertRedirects(response, '/')

# Section for viewing pages that don´t need log in


class Testviews_no_log_in(TestCase):

    def test_menu(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/index.html')

    def test_view_reservation(self):
        response = self.client.get('/my_bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/my_bookings.html')

    def test_view_reservation(self):
        response = self.client.get('/my_bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/my_bookings.html')
