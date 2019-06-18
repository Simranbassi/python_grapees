time=int(input("enter the time  required by the worker (in hours) :"))
if time>=2 and time<=3:
	print(" good efficiency")
elif time>3 and time<=4:
	print("requires improvement in efficiency")
elif time>4 and time<=5:
	print("needs a special improvement training to increase efficiency")
elif time>5:
	print("sorry! you have to leave the company")
else:
	print("invalid input")