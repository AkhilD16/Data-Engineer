'''
1.Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon
'''


str1=input("Enter a String: ")#'Java'
str2=input("Enter a String: ")#'Python'
print(str1,str2)
print(str2[0:2:1]+str1[2:len(str1)+1:1],str1[0:2:1]+str2[2:len(str2)+1:1])

'''
2.Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
	'''


try:
	str=input("Enter a String: ")#'PYTHON'
	if len(str)>=4:
		print(str[0:2:1]+str[len(str)-2:len(str)+1:1])
	else:
		print([])
except:
	print("Input should be String")

'''
3.Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     		  0      1     2      3   4
Let  input  be		  V     A     M     S     I
			         -5    -4    -3    -2    -1

outputs  ---> Character  at  index  0  :  V
			  Character  at  index  1  :  A
			  Character  at  index  2  :  M
			  Character  at  index  3  :  S
			  Character  at  index  4  :  I

			  Character  at  index  -1  :  I
			  Character  at  index  -2  :  S
			  Character  at  index  -3  :  M
			  Character  at  index  -4  :  A
			  Character  at  index  -5  :  V
'''

try:
	str=input("Enter a String: ")
	for x in range(len(str)):
		print("Character at index",x,":",str[x])
	for x in range(-1,-len(str)-1,-1):
		print("Character at index",x,":",str[x])
except TypeError:
	print("Input should be String")

'''
4.Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice


					  0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' =  'Rm a'
'''

try:
	str=input("Enter a String: ")
	even=odd=""
	for x in range(len(str)):
		if x%2==0:
			even=even+str[x]
		else:
			odd=odd+str[x]
	print(odd)
	print(even)
except TypeError:
	print("Intput should be String")

'''
5.If input  are   A   4   B   3   C   2   $   5
                0   1    2   3   4   5   6   7
Output  --->  AAAABBBCC$$$$$
'''

try:
	str=input("Enter a string: ")
	res=""
	for i in range(0,len(str),2):
		ch=str[i]
		num=int(str[i+1])
		res+=ch*num
	print(res)
except (ValueError,TypeError):
	print("Please enter alternate character and digit")




