a=str(raw_input("Enter a string = "))
for i in range(0,len(a)):
	if(i%2==0 and a[i]!= ' ' ):
		print("a["+str(i)+"] = "+str(a[i]))