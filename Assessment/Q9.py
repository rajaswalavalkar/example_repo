import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='Q9log.log',level=logging.DEBUG)

import re
def validate(s):
	x=0							
	if(len(s)>=6 and len(s)<=12):									#length is between 6 to 12
		logging.info('the length was between 6 and 12')
		if re.search("[a-z]",s):
			logging.info('there was a smaller case letter')					#smaller case
			if re.search("[0-9]",s):
				logging.info('there was a number')					#number included
				if re.search("[A-Z]",s):
					logging.info('there was a upper case letter')			#upper case
					if re.search("[$#@]",s):
						logging.info('there was a special character')		#special char
						print("Valid")					#valid password
						x=1
	if(x==0):
		logging.info('there was not a valid password entered')
		print("Not Valid")								#invalid password

def main():
	s = raw_input("Enter your password : ")	
	validate(s)

main()