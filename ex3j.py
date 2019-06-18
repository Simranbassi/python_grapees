side1=int(input("enter the first side of the triangle  :"))
side2=int(input("enter the second side of the triangle   :"))
side3=int(input("enter the third side of the triangle  :"))
sum= side1+side2+side3
if sum==180 :
	print("the tringle is regular")
else:
	print("the triangle is not regular")