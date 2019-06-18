costp=int(input("enter the cost prize of the item"))
sellp=int(input("enter the sell  prize of the item"))
if costp<=sellp :
	profit=sellp-costp
	print("the shopkeeper mde the profit of rupees :",profit)
else :
	loss=costp-sellp
	print("the shopkeeper made the loss of rupees: ",loss)