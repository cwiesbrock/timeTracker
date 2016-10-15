from django.db import models
import datetime

# Create your models here.
class Employee(models.Model):
	number = models.PositiveSmallIntegerField(unique=True, primary_key=True, verbose_name="Personalnummer")
	firstName = models.CharField(max_length=30, verbose_name="Vorname")
	lastName = models.CharField(max_length=30, verbose_name="Nachname") 
	#employmentBegin = models.DateField(blank=True)
	#employmentEnd = models.DateField(blank=True)
	active = models.BooleanField(default=True, verbose_name="aktiv?")
	
	def isPresent(self):
		bookings = Booking.objects.filter(employee=self, dateTime__contains=datetime.date.today())
	
		if ( bookings.filter(type=BookingType.objects.get(type=0)).count() - bookings.filter(type=BookingType.objects.get(type=1)).count()) > 0:
			return True
		else:
			return False
	
	def lastBooking(self):
		booking = Booking.objects.filter(employee=self).order_by('-dateTime')[0]
		return booking
	
	def __str__(self):
		return self.lastName + ", " + self.firstName 
		
class BookingType(models.Model):
	# 0 - kommen
	# 1 - gehen
	type = models.IntegerField(primary_key=True)
	description = models.CharField(max_length=30)
	
	def __str__(self):
		return str(self.type) + " - " + self.description 
	
class Booking(models.Model):
	employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
	dateTime = models.DateTimeField()
	type = models.ForeignKey('BookingType')
	
	def __str__(self):
		return str(self.employee) + " - " + str(self.dateTime) + " - " + str(self.type)