from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .forms import ReservationForm, CommentForm


def date_before():
    if ReservationForm()