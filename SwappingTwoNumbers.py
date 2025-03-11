#Swapping of two numbers without using 3rd variable

a= int(input("Enter first number: "))
b=int(input("Enter Second number: "))
print("Before Swapping: ",a,b)
a,b=b,a
print("After Swapping: ",a,b)

print("-----------------------------------")

#Swapping of two numbers with 3rd variable

a=int(input("Enter first number: "))
b=int(input("Enter Second number: "))
print("Before Swapping: ",a,b)
c=a
a=b
b=c
print("After Swapping: ",a,b)
