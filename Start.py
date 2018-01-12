import random
import sys
import os

print("JAMES")

#this is comment

'''
Multi Line comment
'''
var = 12
name = "David"
print(name)
print("%d" %var)
'''
Variables in Python: Numbers, Strings, Tuples, Lists, Dictionaries
'''
'''
Math operators: + - * / % ** (exponent#) // (floor division?, discards remainder)
'''

# Order. MDAS pa rin

quote = "\"Honesty is "
multi_line_quote = ''' the best policy.'''
complete_quote = quote + multi_line_quote

print("%s %s %s"% (complete_quote, name, 'TEST'))

'''
LISTS
'''


grocery_list = ['tomato', 'banana', 'kulabasa', 'patatas', 12]

print("first = ", grocery_list[0])
print(grocery_list[1:3])

new_order = ['Malan', 'Salol', 'basu', 'Kutsara']

all = [new_order, grocery_list]
print(all)
print(all[0][2])  #displays "basu"

grocery_list.append('Onions') # adds onion at the end
print(grocery_list)

grocery_list.insert(1, 'Tinapay')
print(grocery_list)

grocery_list.remove(12)
print(grocery_list)

grocery_list.sort()
print(grocery_list)

grocery_list.reverse()
print(grocery_list)

del grocery_list[3]
print(grocery_list)

all2 = new_order + grocery_list
print(len(all2))
print(max(all2))
print(min(all2))


'''
=============================================
Tuples( same as list, but cannot be changed after being created)
- use () instead of []
============================================
'''

pi_tuple = (3,1,4,1,5)

new_tuple = list(pi_tuple)
new_tuple.append(9)
print(new_tuple, len(pi_tuple), max(pi_tuple))

'''
=============================================
Dictionaries - key-value pair
same with list, but you cannot join
use {}
============================================
'''

super_hero = {'Batman': 'Bruce',
              'Robin' : 'Damian',
              'Superman': 'Clark'}
print(super_hero['Robin'])
del super_hero['Superman']
print(super_hero)
super_hero['Robin'] = 'Jason'
print(len(super_hero))
print(super_hero.get('Robin'))

print(super_hero.keys())
print(super_hero.values())