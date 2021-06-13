print("30 days 30 hour challenge")
print('30 days 30 hour challenge')

hours = 'thirty'
print(hours)

days = "thirty days"
print(days[0],days[-1])

challenge = 'i will win'
print(challenge[7:10],len(challenge))

challenge = challenge.upper()
print(challenge)
challenge = challenge.lower()
print(challenge)

hours = 'thirty hours'
c = days + hours
d = days+"  "+ hours 
print(c,d,sep="\n")

t = days+' aND '+hours
print(t)
q = t.casefold()
w = q.capitalize()
r = q.find('a')
print(q,w,r,sep="\n")
a = list([q[6].isalpha(),q[6],'isalpha'])
b = list([q[0].isalpha(),q[0],"isalpha"])
q = q+" @5"
print(q)
d = list([q[-1].isalnum(),q[-1],"alnum"])
f = list([q[-2].isalnum(),q[-2],"alnum"])
print(a,b,d,f,sep="\n")


