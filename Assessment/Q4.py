import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='Q4log.log',level=logging.DEBUG)
a=int(raw_input("Enter a number"))
logging.info('a accepted')
s=0
logging.info('s initalized to zero')
while(a!=0):
	s=s+(a%10)
	logging.info('digit added to s')
	a=a/10
	logging.info('last digit removed from a')
print("Sum of digits is = "+str(s))
logging.info('sum of digits printed')