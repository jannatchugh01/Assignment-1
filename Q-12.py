#Write a python program that calculates the sum of the digits of a given number.
# function to find sum
def digits_sum(n):
    sum=0
    for digits in str(n):
        sum+=int(digits)
    return sum
# print output
n=input("Enter the number: ")
print("Sum of digits: ",digits_sum(n))

