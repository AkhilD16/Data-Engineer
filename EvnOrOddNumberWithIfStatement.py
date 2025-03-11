#Program to determine a number is even or odd with if statement

try:
	num=int(input("Enter a Number: "))
	if num%2==0:
		print("entered number: ",num," is even number")
	if num%2==1:
		print("entered number: ",num," is odd number")
except:
	print("Enter valid Number")