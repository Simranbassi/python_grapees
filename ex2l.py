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
sum=a+b+c+d+e
print("sum of the given number [",a,"+",b,"+",c,"+",d,"+",e,"]:",sum)