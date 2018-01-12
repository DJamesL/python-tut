import os
import sys
import random

'''
    FUNCTIONS
'''

def addNum(first, second):
    sum = first + second
    return sum


print(addNum(2,34))
"""
INPUT
"""


print("Enter something")
#jsomething = sys.stdin.readline()
#something = input()
#print("answer", something)


'''
String manipulation
'''
long_str = "ABCDEFGHIJKLMNOPQRTSUVWXYZ"
long_str2 = "A B C D E F G H I J K L M N O P Q R T S U V W X Y Z "

print(long_str[0:4]) #displays ABCD
print(long_str[:-5]) #display everything other than the last 5
print(long_str[-5:]) #displays the last five
print(long_str.find("G")) #outputs index of G
print(long_str.lower()) #sets to lower case
print(long_str.isalpha()) #returns if all items are alphabet
print(long_str.isnumeric()) #returns if all items are numbers
print(len(long_str))
print(long_str.strip()) #remove white spaces


quote_list = long_str2.split(" ")
print(quote_list)
