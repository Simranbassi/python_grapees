order=int(input("enter the number of items to be ordered ::"))
stock=int(input("enter the number of items in stock ::"))
credit=int(input("enter the credit of the customer (enter 1 for ok and 0 for not ok)"))
if credit==1:
else:
	print("not a sufficent credit")
if order<=stock and credit==1:
	print("supply is the requirement")
elif credit!=1:
	print("sorry ! insuffficient credit")
elif credit==1 and stock<order:
	order=order-stock
	print(order)
	print("your total  items to  be shipped are:",order)
else:
	print("invalid policy")