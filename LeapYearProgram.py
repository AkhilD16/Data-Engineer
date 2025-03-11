#Program to Find given year is leap year or not
try:
	year=int(input("Enter year: "))
	if (year%4==0 or year%400==0) and (not year%100==0):
		print(year," is leap year")
	else:
		print(year," is not leap year")
except:
	print("Enter valid year")