l=list()
l=input("Enter list : ")
print(type(l))
for i in range(0,len(l)-1):
	for j in range(i+1,len(l)):
		if(l[i] == l[j]):
			l.remove(l[i])
			
print(l)
