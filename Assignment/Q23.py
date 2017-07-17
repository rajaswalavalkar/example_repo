l=list()
l=input("enter a sorted list : ")
n=int(input("Enter the element to be searched : "))
c=0
for i in range(0,len(l)):
	if(int(l[i]) == n):
		print("Element found at : %d " %i  )
		c=1	
		break
	elif(int(l[i])<n):
		continue
	else:
		c=0;
		break
if(c==0):
	print("NOT FOUND")
		