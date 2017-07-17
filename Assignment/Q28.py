
import re
x=0
st=raw_input("Enter your password : ")	.split(",")
i=0
while(i<len(st)):
	
	x=0
	if(len(st[i])>=6 and len(st[i])<=16):									#length is between 6 to 16
	
		if re.search("[a-z]",st[i]):
							#smaller case
			if re.search("[0-9]",st[i]):
								#number included
				if re.search("[A-Z]",st[i]):
							#upper case
					if re.search("[$#@]",st[i]):
							#special char
						print(st[i])					#valid password
						x=1
	i=i+1
				