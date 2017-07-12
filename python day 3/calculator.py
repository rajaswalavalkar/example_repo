def add(a,b):
	print("ADDITION = "+str(a+b))
def sub(a,b):
	print("SUBTRACTION = "+str(a-b))
def mul(a,b):
	print("MULTIPLICATION = "+str(a*b))
def div(a,b):
	if(b==0):
		print("DIVIDING by ZERO ERROR")
	else:
		print("DIVISION = "+str(a/b))
def mod(a,b):
	print("MODULO = "+str(a%b))
def menu():
	print("\r")
	print("-----MENU-----")
	print("press 1 for addition ")
	print("press 2 for subtraction ")
	print("press 3 for multiplication ")
	print("press 4 for division ")
	print("press 5 for modulo ")
	print("press 6 to EXIT")
	c=input("Enter your choice : ")	
	return c
def firstnum():
	a=input("Enter number 1 :")
	return a
def secondnum():
	b=input("Enter number 2 :")
	return b

while(1):
	c=menu()
	if(c==6):
		break;
	else:
		a=firstnum()
		b=secondnum()
		if(c==1):add(a,b)
		if(c==2):sub(a,b)
		if(c==3):mul(a,b)
		if(c==4):div(a,b)
		if(c==5):mod(a,b)
	
