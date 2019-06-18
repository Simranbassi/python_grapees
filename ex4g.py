a=float(input("enter the percentage of marks in main subject :"))
b=float(input("enter the percentage of marks in subsidiary subject b :"))
if a>=55 and b>=45:
	print("qualified")
elif a<55 and a>=45 and b>55:
	print("qualified")
elif b<=45 and a>=65:
	print("reappear in an examination in B to qualify.")
else:
	print("failed! try again")
