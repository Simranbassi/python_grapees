num=int(input("enter the five digit number"))
print(num)

e=num%10
temp=num//10

d=temp%10
temp=temp//10

c=temp%10
temp=temp//10

b=temp%10
temp=temp//10


a=temp%10
temp=temp//10


print("the reverse of the number is:")
print(a*1+b*10+c*100+d*1000+e*10000)
if a==e and b==d and c==c:
	print("the reverse of the number is same as the given number")
else:
	print("the reverse of the number is not same as the given number")