#Write a program in python that counts the frequency of each character in a string.
str1=input("Enter the string: ")
tup1=tuple(str1)
print (tup1)    # all character in a string
for i in tup1:
   
   res=tup1.count(i)       # count of each character
   print("The count of ",i," is: ",res)