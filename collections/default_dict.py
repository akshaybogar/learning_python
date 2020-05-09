'''
Program to show working of defaultdict
'''

from collections import defaultdict

alphabets = ['a', 'c', 'a', 'd', 'b', 'b', 'a']

'''
#Use a dictionary to store the count of each alphabet in the list
alphabet_counter = {}

for alphabet in alphabets:
    if alphabet in alphabet_counter.keys():#Can be eliminated with defaultdict
        alphabet_counter[alphabet] += 1
    else:
        alphabet_counter[alphabet] = 1

print(alphabet_counter)
'''

alphabet_counter = defaultdict(int)#Creates alphabet_counter dict with default 0
for alphabet in alphabets:
    alphabet_counter[alphabet] += 1

print(alphabet_counter)

#Default value can be specified using lambda function like below
alpha_counter = defaultdict(lambda: 100)
for alphabet in alphabets:
    alpha_counter[alphabet] += 1

print('Default value set to 100', alpha_counter)
