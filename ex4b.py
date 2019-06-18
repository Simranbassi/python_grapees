print("enter 1 for excellent health and 0 for poor health" )
health=int(input("enter the health of the person :"))
if health==1:
	print("excellent health")
elif health==0:
	print("poor health")
else:
	print("not defined")
age=int(input("enter the age of the person :"))
if age<35 or age>25:
	age=1
else:
	age=0
print("press 1 for city and 0 for village")
livein=int(input("enter the area where the person lives:"))
if livein==1:
	print("lives in city")
elif livein==0:
	print("lives in village")
else:
	print("invalid input")
gender=int(input("enter the gender of the person (male or female ) :"))
if age==1: 
	print("you enter male")
elif age==0:
	print("you enter female")
else:
	print("invalid statement")
if health==1 and  age==1 and livein==1 and gender==1:
	print("the premium is Rs. 4 per thousand and his policy amount cannot exceed Rs. 2 lakhs.")
elif health==1 and  age==1 and livein==1 and gender==0:
	print("the premium is Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh")
elif health==0 and  age==1 and livein==0 and gender==1:
	print("the premium is Rs. 6 per thousand and his policy cannot exceed Rs. 10,000")
else:
	print("the person is not insured:")
