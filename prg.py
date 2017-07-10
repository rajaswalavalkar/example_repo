#import sys
a = sys.argv[1].lower()
b = a[::-1]
print(b)
l = len(a)
i=0
c=0
j=l-1
print('string =  ' + a)
while(i<l/2):
	if(a[i]==a[j]):
		c=c+1
	i=i+1
	j=j-1
if(c==l/2):
	print "palindrome"
else:
	print "Not a Palindrome"


