import random
import sys
import os

'''
Conditionals: if-else-elif
== != > < >= <=
'''
age = 21
test_list = ['A', 'b', 'c', 'd', 'e']

if age > 30:
    print("You are old")
elif (age >= 16 and age <= 25):
    print('pasok!')
else:
    print("edi wow")


#LOOPING


for x in range(0, 10):
    print("for loop", x, end="")
print("\n") #add a new line

for y in test_list:
    print(y)

for y in range(0,3):
    print(test_list[y])






num_list = [[1,2,3], [10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

#whiel loops

random_num = random.randrange(0, 20)
while(random_num != 13):
    print(random_num)
    random_num = random.randrange(0, 20)

print("END")
i = 0

while(i<= 20):
    if(i%2 ==0):
        print(i)
    elif(i==9):
        break
    else:
        i+=1
        continue

    i+=1


'''
end 25:00
'''



