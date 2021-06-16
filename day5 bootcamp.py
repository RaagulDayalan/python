l=[2,4,6,5]
l.insert(3,9)
print(l)
l.append(9)
print(l)
del l[2]
print(l)
del l[3:5]
print(l)
l.pop()
print(l)
l=l+[24,3,21,5,8,6,54,0,5,3]
print(l)
a=min(l)
b=max(l)
print('min:',a,'max:',b,sep=' ')
print('min of list:',a,sep=' ')
print('max of list:',b,sep=' ')
a=('hello',1,'o','24',5)
print(a)
print(a[::-1])
b= list(a)
print(b)
b[3] = 'changed'
print(b,a,sep='\n') 

