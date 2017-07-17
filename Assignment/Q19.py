import operator
d = dict()
s=str(raw_input("Enter string : "))
for i in range(0,len(s)-1):
	if(str(s[i]) not in d.keys()):	
		c=1	
		for j in range(i+1,len(s)):
			
			if(s[i]==s[j]):
				c=c+1
		d.update({str(s[i]):str(c)})
l= sorted(d.items(), key=operator.itemgetter(1))
print(l[::-1])