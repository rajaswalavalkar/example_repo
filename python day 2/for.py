'''
1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

import sys
for i in range(1500,2701):
	if(i%7 == 0 and i%5 == 0):
		print(i)
'''

'''
2. Write a Python program to convert temperatures to and from celsius, fahrenheit.

x=raw_input("Degree Celsius(d) or Farenheit(f) : ")
if(x== 'd'):
	a = raw_input("Enter temp in Celsius : ")
	print("Temperature = "+str(((float(a)*9)/5)+32)+" in Farenheit")
	
elif(x == 'f'):
	a = raw_input("Enter temp in Farenheit : ")
	print("Temperature = "+str(((float(a)-32)*5)/9)+" in degree Celsius")

else:
	print("Wrong Input")
'''

'''
3.Write a Python program to construct the following pattern, using a nested for loop.

for i in range (0,6):
	for j in range(0,i):
		print("*"),
	print("\r")
for i in range (0,4):
	for j in range(0,4-i):
		print("*"),
	print("\r")
'''


'''
4.Write a Python program to get the Fibonacci series between 0 to 50

print(0)
print(1)
a=0
b=1
c=1
while(1):
	c=a+b
	if(c>50):
		break
	print(c)
	a=b
	b=c
'''

'''
5.Write a Python program to check the validity of password input by users. Validation :

import re
x=0
s = raw_input("Enter your password : ")
if(len(s)>=6 and len(s)<=16):
	if re.search("[a-z]",s):
		if re.search("[0-9]",s):
			if re.search("[A-Z]",s):
				if re.search("[$#@]",s):
					print("Valid Password")
					x=1
if(x==0):
	print("Invalid Password")
'''

'''
6. print A character	
m=input("Number columns : ")
n=input("Number rows : ")
for i in range(n):
	if(n<=2):
		print("The Letter A cannot be printed if the number of rows are less than 2")
		break
	if(i==0 or i==n/2):
		print("* ")*m 
	else:
		for j in range(0,m):
			if(j==0 or j==m-1):
				print("*"),
			else:
				print(" "),
		print("\r")
'''	


'''
7. print G character
m=input("Number columns : ")
n=input("Number rows : ")
for i in range(n):
	if(i==0):  
		print(" "),	
		print("* ")*(m-2)
	if(i==n-1):
		print(" "),	
		print("* ")*(m-2)
	if(i==n/2):
		print("*"),
		print(" ")*(m/2),
		print("* ")*(m/2) 
	if(i<n/2):
		print("*")
	elif(i>n/2 and i!=n-1):		
		for j in range(0,m):
			if(j==0 or j==m-1):
				print("*"),
			else:
				print(" "),
		print("\r")    		
'''

'''
12.  Write a Python program to calculate a dog's age in dog's years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

m=input("Input a dog's age in human years: ")
print("The dog's age in dog's years is "+str(21+(m-2)*4))
'''

'''
a=raw_input()
print(a)
if a in (str('a') or str('e') or str('i') or str('o') or str('u')):
	print("Vowel")	
'''
'''
m=input("Number columns : ")
n=input("Number rows : ")
for i in range(n):
	if(i<=n/2):
		for j in range(n/2):
			if(j==0):
				print("* "),
				print(" ")*(m-2),
				print("*")
			print("* "),
		print("\r")		
	if(i>n/2):
		for j in range(0,m):
			if(j==0 or j==m-1):
				print("*"),
			else:
				print(" "),
		print("\r")
'''


















