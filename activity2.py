#File in read mode

file_read=open('Codingal.txt','r')
print("File in Read Mode. . .. ")
print(file_read.read())
file_read.close()

#File in write mode
file_write=open('Codingal.txt','w')
file_write.write("File in write mode")
file_write.write("\nHi I am Penguin. . .I am 1 year old")
file_write.close()

#File in append mode
file_append=open('Codingal.txt','a')
file_append.write("\nFile in append mode")
file_append.write("\nWelcome ")
file_append.close()