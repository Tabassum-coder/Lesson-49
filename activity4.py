file1=input("Enter the name of first file")
file2=input("Enter the name of second file")

f1=open(file1,'r')
f2=open(file2,'r')
print("File 1 is \n")
print(f1.read())
print("File 2 is \n")
print(f2.read())
f1.close()
f2.close()

f1=open(file1,'a+')
f2=open(file2,'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)
print("File 1 after adding second file conttent ")
print(f1.read())

f1.close()
f2.close()