from django.contrib import admin
from main.models import Employee, BookingType, Booking
# Register your models here.

admin.site.register(Employee)
admin.site.register(BookingType)
admin.site.register(Booking)