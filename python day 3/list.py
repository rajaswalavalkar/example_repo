l1=["1st month january","2nd month february","3rd month march","4th month april","5th month may","6th month june","7th month july","8th month august","9th month september","10th month october","11th month november","12th month december","1st day monday","2nd day tuesday","3rd day wednesday","4th day thursday","5th day friday","6th day saturday","7th day sunday"]
c=raw_input("enter : ")
for i in l1:
	s=i.split()
	if(str(s[2].lower()) == str(c.lower())):
		print(s[0]+" "+s[1])