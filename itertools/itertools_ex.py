'''
This program shows examples of how to use itertools which is part of python
standard library
'''

import itertools

#Using cycle which is infinite
names = ['Kane', 'Virat', 'Steve', 'Root']
c = itertools.cycle(names)
print(next(c))
print(next(c))
print(next(c))

# Using count from itertools which is also infinite.
#takes 2 parameters initial value and step size which defaults to 1 if left empty
count = itertools.count(100, -5)
print(next(count))
print(next(count))
print(next(count))
