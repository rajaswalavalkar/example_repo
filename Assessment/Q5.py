import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='Q5log.log',level=logging.DEBUG)
l=[1,2,3,4,6,7,8,12]
logging.info('list initialized')
for i in range(0,len(l)):
	logging.info('for loop')
	if(i<len(l)-1):
		logging.info('list is within index')
		s=l[i+1]-l[i]
		if(s!=1):
			logging.info('Missing Value')
			s=s-1
			c=1
			while(s>0):
				print(l[i]+c)
				logging.info('printing missing Values')
				c=c+1
				s=s-1			
	