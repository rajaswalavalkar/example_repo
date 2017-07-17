class MyClass:
   	

	def add(s,a,b):
		print("ADDITION = "+str(a+b))
	
	def sub(s,a,b):
		print("SUBTRACTION = "+str(a-b))

	def mul(s,a,b):
		print("MULTIPLICATION = "+str(a*b))

	def div(s,a,b):
		if(b==0):
			print("DIVIDING by ZERO ERROR")
		else:
			print("DIVISION = "+str(a/b))

	def mod(s,a,b):
		print("MODULO = "+str(a%b))

	def menu(s):
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

	def firstnum(s):
		a=input("Enter number 1 :")
		return a

	def secondnum(s):
		b=input("Enter number 2 :")
		return b
	


mo = MyClass()



while(1):
	c=mo.menu()
	if(c==6):
		break;
	else:
		a=mo.firstnum()
		b=mo.secondnum()
		if(c==1):mo.add(a,b)
		if(c==2):mo.sub(a,b)
		if(c==3):mo.mul(a,b)
		if(c==4):mo.div(a,b)
		if(c==5):mo.mod(a,b)