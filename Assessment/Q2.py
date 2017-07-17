import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='Q2log.log',level=logging.DEBUG)
c="A"
i=0
j=0
while(i<5):
	j=0
	logging.info('j initalized to zero')
	while(j<=i):
		
		print(c),
		c=chr(ord(c) + 1)
		j=j+1
	print("\r")
	i=i+1