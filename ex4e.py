side1=int(input("enter the first side of the triangle :"))
side2=int(input("enter the second side of the triangle :"))
side3=int(input("enter the third side of the triangle :"))
if side1>side2 and side1>side3:
	largest=side1
elif side2>side1 and side2>side3:
	largest=side2
elif side3>side1 and side3>side2:
	largest=side3
print(largest)
if largest>side1+side3 or largest>side1+side2 or largest>side2+side3:
	print("valid triangle")
else:
	print("invalid triangle")