# String Object...
a='Akhil Dhamarakonda'
print(a)
print(a[:])
print(a[::-1])
print(a[2:5])
print(a[-1:-9:-1])
print(len(a))

#int() funtion
print(int(True))
print(int(0b0011001))
print(int(26.9))
print(int(0xabe29))
print(int(0o2345))
#print(int('Akhil')) #Error...
#print(int(3+4j)) #Error... 


#float() funtion
print(float(25))
print(float(True))
print(float(0b0110010))
print(float(0o2345))
print(float(0xabe29))
#print(float('Akhil')) #Error..
#print(float(3+4j))#Error..

#complex() function
print(complex(25))
print(complex(18.0))
print(complex(18j))
print(complex(True,False))
print(complex(True))
print(complex(False))
#print(complex('Akhil')) #Eror
print(complex('3'))
print(complex('4j'))
#print(complex(3,'4j')) # Second argument cant be string

#bool() funtion....
print(bool(21))
print(bool(-21))
print(bool(0))
print(bool('Akhil'))
print(bool(0+0j))
print(bool(0.1))
print(bool(1+0j))

#Range Object
a=range(1,10,1)
print(a)
print(*a)
b=range(10,100,10)
print(b)
print(*b)
print(*range(1,50,2))
print(*range(2,50,2))
print(*a[1:9:2])
c=range(True,10,1)
print(*c)
print(*a[::-1])

#List[] object
a=[]
a.append(123)
a.append('Akhil')
a.append(3+4j)
a.append(18.5)
print(*a)
a.remove(a[0])
a.remove(a[2])
print(*a)
a[1]=123
a[0]='virat'
print(*a)
#a[2]='cricket'
#print(*a)#Error (index out f range)
b=[18,39,'akhil',36.0,'ravi']
print(*b)
print(*b[::-1])

#Tuple Object...
a=('akhil',12,18.9)
print(*a)
#a.add('Banti')#Error
print(*a)

#Dictionary Object..
 #how to print dictionary in different ways...	
a={10:'Akhil',20:'Raju',30:'Ram',40:'Sita'}	
print(a)
print(type(a))
print(a[10])
print(a[20])
print(a[30])
print(a[40])
#print(a[15]) # KeyError.....
#print(a.['Akhil']) #We cant use values to access keys and returns Error..
a[20]='Virat'
print(a)
a[12]='Rohit'
print(a)
print(len(a))
del a[12]
print(a)
#print(a*2)  #Error
