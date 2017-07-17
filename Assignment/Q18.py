a=str(raw_input("enter a string = ")).split()
c=len(a)-1
while(c>=0):
	i=a[c]
	print(i[::-1]+" "),
	c=c-1
