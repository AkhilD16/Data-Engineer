#Program to print natural numbers (1,2,3,4,.....,10)
num=int(input("Enter a number: "))
print("Natural Numbers:")
for i in range(1,num+1):
	print(i)

print('------------------------------------')

#Natural numbers in Reverse order(10,9,8,.....,1)
num=int(input("Enter a number: "))
print("Natural Numbers in reverse order:")
for i in range(num,0,-1):
	print(i)
