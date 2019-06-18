print("enter the conditions for the steel")
hardness=int(input("input the hardness of steel:"))
if hardness>50:
	hardness=1
else:
	hardness=0
cc=int(input("input the carbon content of steel:"))
if cc<0.7:
	cc=1
else:
	cc=0
ts=int(input("inut the tensile strength of steel:"))
if ts>5600:
	ts=1
else:
	ts=0
if hardness==1 and cc==1 and ts==1:
	print("steel has grade 10")
elif hardness==1 and cc==1 and ts==0:
	print("steel has grade 9")
elif hardness==0 and cc==1 and ts==1:
	print("steel has grade 8")
elif hardness==1 and cc==0 and ts==1:
	print("steel has grade 7")
elif  hardness==1 or cc==1 or ts==1:
	print("steel has grade 6")
elif hardness==0 and cc==0 and ts==0:
	print("steel has grade 5")
else:
	print("invlid =")