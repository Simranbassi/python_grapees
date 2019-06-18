year=int(input("enter the year "))
if year%4==0:
	print("the year you enter is a leap year")
elif year%400==0:
	print("the year you enter is a leap year")
else:
	print("the year you enter is not a leap year")