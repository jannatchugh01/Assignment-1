#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input. 
print("Temperature Conversion: ")
print("1 = Celsius to Fahrenheit")
print("2 = Fahrenheit to Celsius")
Input=input("Enter input for conversion: ")
num=int(input("Enter temperature: "))
CTF=float((num * 1.8)+32)  #degree to fahrenheit
FTC=float((num-32)/1.8 )# fahrenheit to degree
if("Input==1"):
    print("{} C={} F".format(num,CTF))
else:
    print("{} F={} C".format(num,FTC))