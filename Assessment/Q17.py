class Circle:
	def __init__(s,r):
		s.r=r
	def area(s):
		return(3.14*s.r*s.r)

r=int(raw_input("Enter your radius : "))
c=Circle(r)
print(c.area())