#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
str1=int(input("Enter first number: "))
str2=int(input("Enter second number: "))
print("Select operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
opt=input("Enter choice(1,2,3,4): ")
if(opt=='1'):
    print("Sum of number: ",str1+str2)
elif(opt=='2'):
    print("Difference of number: ",str1-str2)
elif(opt=='3'):
    print("Multiply of number: ",str1*str2)
elif(opt=='4'):
    print("Division of number: ",str1/str2)
else:
    print("Not a valid operator")