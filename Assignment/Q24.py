import sys
l1=list()
for i in range(1,len(sys.argv)):
	if (sys.argv[i]>=str(0) and sys.argv[i]<=str(9)):
		l1.append(sys.argv[i])
print(l1)