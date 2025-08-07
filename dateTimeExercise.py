from datetime import datetime
birthday = datetime(1993, 8, 16, 23, 20, 55, 68)
print(birthday.year)
print(birthday.weekday())
print(birthday.hour)

print(datetime.now())
subtraction = datetime(2008, 1, 1) - birthday
print(subtraction)
print(datetime.now() - birthday)

parsed_date = datetime.strptime("Jan 15, 2018", "%b %d, %Y")
print(parsed_date)
print(parsed_date.year)

date_string = datetime.strftime(datetime.now(), "%b-%d-%Y")
print(date_string)

