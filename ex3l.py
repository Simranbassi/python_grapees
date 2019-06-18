length=int(input("enter the length of the rectangle : "))
breadth=int(input("enter the breadth of the rectangle: "))
area=length*breadth 
print("the area of the rectangle is :",area)
perimeter=2*(length+breadth)
print("the perimeter of the rectangle is :",perimeter)
if area>perimeter:
	print("the area of the rectangle is greater")
else:
	print("the perimeter of the rectangle is greater")


