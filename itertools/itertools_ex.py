'''
This program shows examples of how to use itertools which is part of python
standard library
'''

import itertools

#Useing cycle which is infinite
names = ['Kane', 'Virat', 'Steve', 'Root']
c = itertools.cycle(names)
print(next(c))
print(next(c))
print(next(c))
