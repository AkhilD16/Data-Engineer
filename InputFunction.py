#input() function:--> input() function used to take the inputs from the user while runtime.
					#-->>Irrespective of the user inputs it always reads the input as string.
					#-->To convert that string to other object,we have to perform typecasting.
a=input("Enter any Value: ")#int 123
print(a)#string 123
print(type(a)) #<class str>
b=input("Enter any Value: ")#float 10.8
print(b)#string 10.8
print(type(b)) #<class str>
c=input("Enter any value: ")#list [10,20,30,40]
print(c)#string [10,20,30,40]
print(type(c))#<class str>
