class Person:
	def getGender(s,g):
		print("Gender = "+str(g))

class Male(Person):
	def getGender(s,g):
		print("Gender = "+str(g))

class Female(Person):
	def getGender(s,g):
		print("Gender = "+str(g))

x=Male()
y=Female()
print(x.getGender("Male"))
print(y.getGender("Female"))