year=int(input("enter the year which you want see as a lep or non leap year: "))
if year%400==0 or year%4==0:
	print("the year you enter is a leap year")
else:
	print("the year you enter is not a leap year")
	