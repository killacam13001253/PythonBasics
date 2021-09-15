introstring=input("enter you introduction")
charatercount=0
wordcount=1
for i in introstring:
    charatercount=charatercount+1
    if(i==' '):
        wordcount=wordcount+1
print("number of word in string")
print(wordcount)
print("number of character in the string")
print(charatercount)