#Write a program that takes a string input from the user and writes it to a text file
samplefile=open("D:/Coding/python/Assignment-1/file.txt","w")
text=input("Enter the text :")
print(text, file=samplefile)