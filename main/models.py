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

#	Ermittelt, ob der Mitarbeiter aktuell anwesend ist
	def isPresent(self):
		bookings = Booking.objects.filter(employee=self, begin__contains=datetime.date.today(), delete=False).order_by('-begin')[:1]

		if bookings.count() == 0 or (bookings[0].end != None):
			return False
		else:
			return True

	# Ermittelt die letzte Buchung des Mitarbeiters
	def lastBooking(self):
		booking = Booking.objects.filter(employee=self, delete=False).order_by('-begin')
		if booking.count() > 0:
			return booking[0]
		else:
			return None

	# Ermittelt den Zeitpunkt der letzen Aktivität
	def latestActivity(self):
		if self.lastBooking() == None:
			return None
		elif self.lastBooking().end == None:
			return self.lastBooking().begin
		else:
			return self.lastBooking().end

	def __str__(self):
		return self.lastName + ", " + self.firstName

class BookingType(models.Model):
	# 0 - Standard
	type = models.IntegerField(primary_key=True)
	description = models.CharField(max_length=30)

	def __str__(self):
		return str(self.type) + " - " + self.description

class Booking(models.Model):
	employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
	begin = models.DateTimeField(blank=True)
	end = models.DateTimeField(blank=True, null=True)
	type = models.ForeignKey('BookingType')
	delete = models.BooleanField('gelöscht', default=False)

	def __str__(self):
		return str(self.employee) + " - " + self.begin.strftime('%x - %X') + " - " + str(self.id) + " - " + str(self.type)
