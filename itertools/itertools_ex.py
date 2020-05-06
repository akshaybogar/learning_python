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

# Using accumulate from itertools
#Accumulator by default adds values to the number that occured before
values = [1, 2, 3, 10, 4, 2, 1]
acc = itertools.accumulate(values)
print(list(acc))

# Other functions such as max can also be passed.
acc1 = itertools.accumulate(values, max)
print(list(acc1))

#Using dropwhile and takewhile from itertools
#creating utility function
def test(x):
    return x>4

vals = [11, 5, 7, 12, 4, 6, 2]
print(list(itertools.takewhile(test, vals)))
print(list(itertools.dropwhile(test, vals)))
