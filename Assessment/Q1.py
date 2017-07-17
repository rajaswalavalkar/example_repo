import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='Q5log.log',level=logging.DEBUG)
a=int(raw_input("Enter a number 1 = "))
b=int(raw_input("Enter a number 2 = "))
print(int(a/b))					#dividing By zero runtime error

