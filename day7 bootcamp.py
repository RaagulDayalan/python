def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
a,b=map(int,input("Enter the two numbers: ").split())
print("Addition of",a,"and",b,'=',add(a,b))
print("Subtraction of",b,"from",a,'=',sub(a,b))
print("Multiplication of",a,"and",b,'=',mul(a,b))
print("Division of",a,"by",b,'=',div(a,b))




def covid():
    a=str(input("Enter the Patient Name:"))
    b=float(input("Enter the temperature:"))
    c=input("do you have troubles breathing (y/n):")
    if(b>=101 and c == 'y'):
        print("u may have covid get tested")
    
    

covid()
