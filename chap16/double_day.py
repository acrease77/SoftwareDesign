from datetime import *

def current_date():
	today=datetime.today()
	print today
	print today.strftime('%A')

#print current_date()

def birthday_countdown(birthday):
	today=datetime.today()
	birthday_this_year=datetime(today.year,birthday.month,birthday.day)
	if today>birthday_this_year:
		next_birthday=datetime(today.year+1,birthday.month,birthday.day)
	else:
		next_birthday=birthday_this_year
	days_until=next_birthday-today
	return days_until, 'until your birthday on', next_birthday

birthday=datetime(1994,11,10)

#print birthday_countdown(birthday)

def double_day(birthday1,birthday2,n):
	if birthday1>birthday2:
		latestbirth=birthday1
		firstbirth=birthday2
	elif birthday2>birthday1:
		latestbirth=birthday2
		firstbirth=birthday1
	difference=latestbirth-firstbirth
	double_day=latestbirth+(n-1)*difference
	return double_day

b1=datetime(1994,11,10)
b2=datetime(1963,10,22)
print double_day(b1,b2,2)