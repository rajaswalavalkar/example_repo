import operator
s=raw_input("Enter a sentence : ").split(" ")
l1=dict()
for i in range(0,len(s)):
	c=1
	if(str(s[i]) not in l1.keys()):	
		for j in range(i+1,len(s)):		
			if(s[i]==s[j]):
				c=c+1
		l1.update({str(s[i]):str(c)})
		#print(str(s[i])+" "+str(c))



l= sorted(l1.items(), key=operator.itemgetter(0))
print(l)


