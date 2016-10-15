from django import template
from main.models import Employee
from django.utils.safestring import mark_safe
import datetime

register = template.Library()

@register.filter(name='isPresent')
def isPresent(value):
	employee = Employee.objects.get(number=value)
	return employee.isPresent()
	
@register.filter(name='Presence')
def Presence(value):
	employee = Employee.objects.get(number=value)
	if employee.isPresent():
		return mark_safe('<span class="green">anwesend</span> <span class="glyphicon glyphicon-stop green"></span>')
	else:
		return mark_safe('<span class="red">abwesend</span> <span class="glyphicon glyphicon-stop red"></span>')
		
@register.filter(name='lastBooking')
def lastBooking(value):
	employee = Employee.objects.get(number=value)
	return employee.lastBooking()
	
@register.filter(name='getBookingDate')
def getBookingDate(value):
	return value.dateTime

@register.filter(name='getBookingType')
def getBookingType(value):
	return value.type.description
	
@register.filter(name='getBookingDateText')
def getBookingDateText(value):
	dateDiff = (datetime.datetime.now() - value).days

	if dateDiff == 0:
		ReturnStr = "Heute"
	elif dateDiff == 1:
		ReturnStr = "Gestern"
	elif dateDiff == 2:
		ReturnStr = "Vorgestern"
	elif (dateDiff > 2 and dateDiff < 7):
		ReturnStr = "vor " + str(dateDiff) + " Tagen"
	else:
		ReturnStr = value.strftime('%d.%m.%Y')
		
	return ReturnStr