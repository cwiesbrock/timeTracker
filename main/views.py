# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Employee, Booking, BookingType
from operator import itemgetter
import datetime
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	employees = Employee.objects.filter(active=True).order_by('lastName', 'firstName')
	return render(request, 'index.html', {'employees': employees})

def detail(request, employeeNo, status=""):
	bookingPairs = []

	employee = Employee.objects.get(number=employeeNo)
	bookings = Booking.objects.filter(employee=employeeNo, begin__gte=datetime.datetime.now()-datetime.timedelta(days=30), delete=False).order_by('-begin')

# Buchungen der letzten 30 Tage ausgeben
	for booking in bookings:
		# Fehler-Hineweis setzen, falls Gehen- oder Kommen-Buchung fehlen
		if booking.begin == None:
			comment = 'Kommen-Buchung fehlt'
			bookingStatus = 'E'
			total = ''
		elif booking.end == None:
			# Eine Buchung ohne Gehen-Buchung für den aktuellen Tag ist kein Fehler
			if booking.begin.strftime('%d.%m.%Y') != datetime.datetime.now().strftime('%d.%m.%Y'):
				print(datetime.datetime.now().strftime('%d.%m.%Y'))
				comment = 'Gehen-Buchung fehlt'
				bookingStatus = 'E'
			else:
				comment = ''
				bookingStatus = ''
			total = ''
		else:
			comment = ''
			bookingStatus = ''
			total = (booking.end.replace(microsecond=0) - booking.begin.replace(microsecond=0))

		# Nur Buchungen die weniger als 7 Tage alt sind dürfen durch den User verändert werden
		if booking.begin >= datetime.datetime.now() - datetime.timedelta(days=7):
			aktion = True
			deleteOnClick = "redirect('/employee/" + str(booking.employee.number) + "/booking/" + str(booking.id) + "/delete/',0);"
		else:
			aktion = False
			deleteOnClick = ""


		bookingPair = {'date': booking.begin.date, 'in':booking.begin, 'out': booking.end, 'total': total, 'comment': comment, "bookingStatus": bookingStatus, "aktion": aktion, "id": booking.id, "deleteOnClick": deleteOnClick}
		#print(bookingPair)
		bookingPairs.append(bookingPair)

	return render(request, 'detail.html', {'employees':employee, 'bookingPairs': bookingPairs, 'status': status, 'now':datetime.datetime.now()})

def booking(request, employeeNo, bookingId, operation):
	try:
		booking = Booking.objects.get(id=bookingId, delete=False)
	except Booking.DoesNotExist:
		booking = None

	if booking != None:
		booking.delete = True
		booking.save()
		statusText = "Buchung " + str(bookingId) + " erfolgreich gelöscht"
		statusType = 'alert-success'
	else:
		statusText = "Buchung " + str(bookingId) + " nicht gefunden"
		statusType = 'alert-danger'

	status = {'message':statusText, 'type': statusType}

	# return detail(request, employeeNo, status)
	return HttpResponseRedirect(redirect_to='/employee/' + employeeNo)

def book(request, employeeNo, operation):
	employee = Employee.objects.get(number=employeeNo)

	if operation=="start":
		booking = Booking(employee = employee, begin = datetime.datetime.now(), type = BookingType.objects.get(type=0))
		booking.save()
	else:
		booking = employee.lastBooking()
		booking.end = datetime.datetime.now()
		booking.save()

	status = {'message':"Buchung erfolgreich - automatische Weiterleitung zur Übersichtsseite in 3 Sekunden", 'redirect':"/", 'redirectDelay':3, "type": "alert-success"}

	return detail(request, employeeNo, status)

def employeePresent(employeeNo):
	employees = Employee.objects.get(number=employeeNo)
	return True
