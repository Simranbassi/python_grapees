num=int(input("enter the four digit number"))

d=num%10
num=num//10

c=num%10
num=num//10

b=num%10
num=num//10

a=num%10
num=num//10

sum=a+d
print("the sum of the first and the last digit is:",sum)