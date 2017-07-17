list =[(2,5),(1,2)]
o=sorted(list,key = lambda x:x[-1])
i=len(o)-1
while(i>=0):
	print(o[i]),
	i=i-1