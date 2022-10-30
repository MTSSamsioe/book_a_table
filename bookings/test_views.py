from django.test import TestCase
from .models import Reservation, Comments
from django.contrib.auth.models import User

# Create your tests here.
class Testviews(TestCase):
    
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/index.html')

    def test_view_reservation(self):
        response = self.client.get('/my_bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/my_bookings.html')


    # def test_edit_reservation(self):
    #     reservation = Reservation.objects.create({
    #         'first_name': 'first',
    #         'last_name': 'last',
    #         'email': 'email@emial.com',
    #         'date_time': '2002-11-15 15:00',
    #         'number_of_guests': 2,
    #         }))
    #     response = self.client.get(f'/edit/{reservation.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'bookings/edit.html')

    # def test_can_add_resevation(self):
    #     #test_user = self.client.login(username='testuser', password='testpw')
    #     response = self.client.post('/my_bookings/add', {
    #         'first_name': 'first',
    #         'last_name': 'last',
    #         'email': 'email@emial.com',
    #         'date_time': '2002-11-15 15:00',
    #         'date_time_end': '2002-11-15 17:00',
    #         'number_of_guests': '2',
    #         'number_of_tables': '1',
    #         'status': '1'

    #         })
    #     self.assertRedirects(response, '/my_bookings/')

    
    # def test_can_delete_reservation(self):
    #     reservation = Reservation.objects.create(first_name= 'hej')
    #     self.assertRedirects(response, '/my_bookings/')

    def test_menu(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        

    # def test_add_comment(self):
    #     test1 = User.objects.create_user.self.client.login(username='testuser', password='testpw')
    #     login = self.client.login(username='testuser', password='12345')
    #     comment = Comments.objects.create(user='test1', created='2022-10-01 13:00',text='Test',approved='1' ,stars='3' )
    #     self.assertRedirects(response, '/add_comment/')
