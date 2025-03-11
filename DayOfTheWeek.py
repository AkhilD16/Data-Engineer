'''#Progra to print day of the week
let input be : 4
Output---> Thursday'''

try:
	day=int(input("Enter a number: "))
	match day:
		case 1:
			print("Monday")
		case 2:
			print("Tuesday")
		case 3:
			print("Wednesday")
		case 4:
			print("Thursday")
		case 5:
			print("Friday")
		case 6:
			print("Saturday")
		case 7:
			print("Sunday")
		case _:
			print("Invalid")
except:
	print("Input should be an ineteger") 
		