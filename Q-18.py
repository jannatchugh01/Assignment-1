#Write a python program that checks if two strings are anagrams of each other.
str1="NewYork Times"
str2="monkeys write"
print("First string: ",str1)
print("Second string: ",str2)
list1=list(str1.upper())
print(list1)
list2=list(str2.upper())
print(list2)
sort1=list1.sort()
sort2=list2.sort()
if(sort1==sort2):
    print("Both strings are anagrams")
else:
    print("They are not anagrams")