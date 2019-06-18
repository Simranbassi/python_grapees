num=int(input("enter the five digit number"))
e=num%10
num=num//10

d=num%10
num=num//10

c=num%10
num=num//10

b=num%10
num=num//10

a=num%10
num=num//10

e=e*10000
d=d*1000
c=c*100
b=b*10
a=a*1
rev=a+b+c+d+e
print("rev of the given number is",rev)
