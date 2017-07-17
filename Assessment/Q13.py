def even(n):
	return(int(n)/2)

def odd(n):
	return((3*int(n))+1)

a=raw_input("Enter a nunber")
l=list()
i=1
while(a!=1):
	if(int(a)%2==0):
		a=even(a)
		print(a),
		i=i+1
	else:
		a=odd(a)
		print(a),
		i=i+1

	