s=str(raw_input("Enter string : "))
c=0
d=0
for i in s:
	if(i >= 'a' and i <= 'z'):
		c=c+1
	if(i >= 0 and i <= 9):
		d=d+1
print("Number of letters  = "+str(c))
print("Number of integer = "+str(d))