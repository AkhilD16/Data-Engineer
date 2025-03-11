#1.Program to replace every occurence of first character in the string with '*' except first charcter

str=input("Enter a string: ")
res=str
for i in range(len(str)):
	for j in range(i+1,len(str)):
		if str[i]==str[j]:
			res=res[:j]+'*'+res[j+1:]
print(res)

'''
2.Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  --->  interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself

'''
str=input("Enter a string: ")
if len(str)<3:
	print(str)
elif str.endswith('ing'):
	print(res:=str+'ly')
elif not str.endswith('ing'):
	print(res:=str+'ing')


