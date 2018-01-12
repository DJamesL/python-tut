import os
import sys


'''
File IO
'''

test_file = open("test.txt", "wb")
test_file2 = open("test2.txt", "a")
'''
                 | r   r+   w   w+   a   a+
------------------|--------------------------
read              | +   +        +        +
write             |     +    +   +    +   +
write after seek  |     +    +   +
create            |          +   +    +   +
truncate          |          +   +
position at start | +   +    +   +
position at end   |                   +   +

add "b" if in binary format
truncate = erase everthing before reading or writing

'''

print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Entered from pyCharm. \n", 'UTF-8'))
#test_file2.write(bytes("Entered from pyCharm. \n", 'UTF-8'))
test_file2.write("JAMES POGI")
test_file.close()
test_file2.close()

test_file = open("test.txt", "r")
text_in_file = test_file.read()
print(text_in_file)
test_file.close()

os.remove("test.txt")
os.remove("test2.txt")