from django.shortcuts import render
from .models import Employee, Booking, BookingType
import datetime


# Create your views here.

def index(request):
	employees = Employee.objects.all().order_by('lastName', 'firstName')
	return render(request, 'index.html', {'employees': employees})

def detail(request, employeeNo, status=""):
	bookingPairs = []
	inBooking = None
	outBooking = None
	
	employees = Employee.objects.get(number=employeeNo)
	bookings = Booking.objects.filter(employee=employeeNo).order_by('dateTime')
	bookingTypeIn = BookingType.objects.get(type=0)
	
# Buchungen zu Kommen-Gehen-Paaren zusammenfassen und Arbeitszeit berechnen
	for booking in bookings:

		#print(booking.type)
		if booking.type == bookingTypeIn: 	#Kommen-Buchung
			if inBooking != None:
				print("Gehen-Buchung fehlt")
				bookingPair = {'date': inBooking.dateTime.date, 'in':inBooking.dateTime, 'out': "", 'total': ""}
				bookingPairs.append(bookingPair)
			inBooking = booking
		else:					#Gehen-Buchung
			outBooking = booking
			
		if inBooking != None and outBooking != None:
			bookingPair = {'date': inBooking.dateTime.date, 'in':inBooking.dateTime, 'out': outBooking.dateTime, 'total': outBooking.dateTime - inBooking.dateTime}
			bookingPairs.append(bookingPair)
			inBooking = None
			outBooking = None

	return render(request, 'detail.html', {'employees':employees, 'bookings': bookings, 'bookingPairs': bookingPairs, 'status': status, 'now':datetime.datetime.now()})

def book(request, employeeNo, operation):
	employee = Employee.objects.get(number=employeeNo)
	
	if operation=="start":
		bookingType = BookingType.objects.get(type=0)
	else:
		bookingType = BookingType.objects.get(type=1)
		
	booking = Booking(employee = employee, dateTime = datetime.datetime.now(), type = bookingType)
	booking.save()
	
	status = {'message':"Buchung erfolgreich - automatische Weiterleitung zur Übersichtsseite in 3 Sekunden", 'redirect':"/", 'redirectDelay':3}
	
	return detail(request, employeeNo, status)

def employeePresent(employeeNo):
	employees = Employee.objects.get(number=employeeNo)
	return True
	