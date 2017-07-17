import sys
i=1
s=0
while(i<len(sys.argv)):
	if(str(sys.argv[i]) == 'D'):
		s=s+int(sys.argv[i+1])
	if(str(sys.argv[i]) == 'W'):
		s=s-int(sys.argv[i+1])
	i=i+2
	
print(s)