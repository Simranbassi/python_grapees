day=int(input("enter the number of days the member is late: "))
if day<=5:
	print("you have a fine of rupees 50 paise")
elif day>5 and day<=10:
	print("you have a fine of 1 rupees  ")
elif day>10 and day<30:
	print("you have a fine of 5 rupees ")
elif day>30:
	print("your member ship has been cancelled")
else:
	print(":::invalid input:::")