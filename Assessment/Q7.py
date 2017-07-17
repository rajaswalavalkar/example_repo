class MyException(Exception):    
    def __init__(s, v):
        s.v = v    
    def __str__(s):
        return(repr(s.v))
 
try:
    a=2
    b=0
    if(b==0):
    	raise(MyException("Dividing by zero"))

except MyException as error:
    print('A New Exception occured: ',error.v)