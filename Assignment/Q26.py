class MyException:
	def __init__(self,s):
		self.s=s
		print("The error message is : "+str(self.s))
		
mes=str(raw_input("enter a message : "))
m = MyException(mes)