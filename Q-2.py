# Write a program that checks whether a given number is even or odd

num=int(input("Enter the number :"))
if(num%2)==0:
    print("Even Number")
elif(num%2)!=0:
    print("Odd Number")
else:
    print("Not an integer")