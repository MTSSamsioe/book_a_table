from django.contrib import admin

from .models import *


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'approved', 'text', 'stars')

    actions =['Approve_comment', 'Disapprove_comment']

    def Approve_comment(self, request, queryset):
        queryset.update(approved = True)

    def Disapprove_comment(self, request, queryset):
        queryset.update(approved = False)


admin.site.register(Comments,CommentAdmin )


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user','first_name', 'last_name', 'date', 'number_of_guests', 'status')

    actions =['Approve_reservation', 'Disapprove_reservation']

    def Approve_reservation(self, request, queryset):
        queryset.update(status = True)

    def Disapprove_reservation(self, request, queryset):
        queryset.update(status = False)

admin.site.register(Reservation, ReservationAdmin )