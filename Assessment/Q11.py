l = raw_input("Enter a sequence of numbers : ")
a=l[0]
b=l[1]
i=2
c=0
while(i<len(l)-1):
	
	if((int(a)+int(b))!=int(l[i])):
		if(int(a)+int(b)==int(l[i]+l[i+1]) and (i+1)<=len(l)-1):
			a=b
			b=int(l[i])*10+int(l[i+1])
			i=i+2
			continue
		c=1	
		break
	else:
		a=b
		b=l[i]
	
	i=i+1

if(c==0):
	print("Additive Sequence")
else:
	print("Not an Additive Sequence")