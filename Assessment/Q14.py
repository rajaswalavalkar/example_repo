n=int(input("Enter a number"))
i=1
while(i<=n):
	if(2**i==n):
		print("Power")
		f=1
		break		
	else:	
		f=0	
		i=i+1
if(f==0):print("Not power")
