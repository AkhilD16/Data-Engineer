#eval() function :---> This function converts String to it's corresponding object.
x=25
a=eval('10.4')
print(a)
print(type(a))
y=eval('x')
print(type(y))
z= eval('3+4j')
print(z)
print(type(z))
b=eval('[10,20,30,40]')
print(b)
print(type(b))
c={10:'Akhil',20:'Virat'}
print(c)
print(type(c))
d=eval("{10:'Akhil',20:'Virat'}")
print(d)
print(type(d))
e=eval("range(1,10,2)")
print(*e)
print(type(e))

# F string:--> F standsfor Format and this converts any python object into String object.

f=25
print(type(f))
g=F'{f}'
print(f'{g=}')
print(type(g))
h=range(1,10,2)
print(*h)
print(type(h))
i=f'{h}'
print(i)
print(type(i))

