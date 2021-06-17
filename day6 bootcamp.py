a={'chennai':'csk','Bangalore':'rcb','punjab':'kxip','mumbai':'mi'}
b={'rajastan':'rr'}
c=a|b
print(c)

a={'chennai':'csk','Bangalore':'rcb','punjab':'kxip','mumbai':'mi'}
b={'rajastan':'rr'}
a.update(b)
print(a)

del a['rajastan']
print(a)

a=[0,1,2,3,4]
b=['chennai','mumbai','delhi','calcutta','andhra']
c={}
for i in a:
    c[i]=b[i]

print(c)

d=set(b)
print(b)
print(d)

print(len(d))

e={'delhi', 'chennai'}

for i in e:
    d.remove(i)

print(d)



