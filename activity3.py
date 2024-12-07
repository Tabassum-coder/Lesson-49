file=open('Codingal.txt','r')
Counter=0
content=file.read()
CoList=content.split("\n")

for i in CoList:
    Counter+=1

print("Number of lines in file is ",Counter)