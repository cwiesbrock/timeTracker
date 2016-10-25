import datetime

def dateToText(value):
	dateDiff = (datetime.datetime.now().replace(microsecond=0, second=0, minute=0, hour=0) - value.replace(microsecond=0, second=0, minute=0, hour=0)).days

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
