from django.test import TestCase
from django.contrib.auth.models import User
from .forms import CommentForm, ReservationForm
from .models import Reservation, Comments
from datetime import datetime

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
