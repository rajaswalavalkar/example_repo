l=list()
l=input("Enter a list :  ")
l=[l[x] for x in range(0,len(l)) if x%2==0]
print(l)
