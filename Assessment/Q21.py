fp = open("File.txt","r+")
content = fp.readlines()
for item in content[::-1]:
	print item