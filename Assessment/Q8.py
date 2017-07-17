import math 
class Number:
	 
    def __init__(s, n):
        s.__n = n
      
    def getNumber(s):
        return s.__n
 
    def __add__(s, a_n):
        return Number( s.__n + a_n.__n )
 
n1 = Number(4)
print("Number  = "+str(n1.getNumber()))
 
n2 = Number(5)
print("Number = "+str(n2.getNumber()))
 
n3 = n1 + n2 
print("Addition = "+str(n3.getNumber()))