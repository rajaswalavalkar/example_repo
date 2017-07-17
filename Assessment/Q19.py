class Str:
	
	def acc(s):
		s.string = str(raw_input("Enter a string : "))

	def prnt(s):
		print("The string entered : "+s.string)

s1=Str()
s1.acc()
s1.prnt()