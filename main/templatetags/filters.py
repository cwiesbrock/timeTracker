from django import template
from main.models import Employee
from django.utils.safestring import mark_safe
import datetime
from ..helper import dateToText

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

	if employee.lastBooking() != None:
		return mark_safe('<span>Letze Buchung: ' + dateToText(employee.latestActivity()) + ', um ' + employee.latestActivity().strftime('%H.%M') + '</span>')
	else:
		return mark_safe('<span>Keine Buchungen vorhanden</span>')

@register.filter(name='getBookingDate')
def getBookingDate(value):
	return value.begin

@register.filter(name='getBookingType')
def getBookingType(value):
	return value.type.description
