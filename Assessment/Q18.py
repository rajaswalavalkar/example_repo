class ListView:
	def __init__(s,l1):
		s.l1=l1

	def app(s,a):
		s.l1.append(a)
		print(s.l1)

	def dell(s,a):
		s.l1.remove(a)
		print(s.l1)

l1=[1,2,3]
cl=ListView(l1)
a=int(input("Enter number to be added : "))
cl.app(a)
a=int(input("Enter number to be deleted : "))
cl.dell(a)

