from collections import Counter

list1 = ['a', 'b', 'd', 'c', 'e', 'a', 'a', 'a', 'c', 'c', 'd']
list2 = ['d', 'd', 'e', 'e', '']

# Create counter objects by passing list1 and list2
c1 = Counter(list1)
c2 = Counter(list2)

# Check number of a's in list1
print(c1['a'])

# Total number of alphabets in l1
print(sum(c1.values()), 'no. of alphabets are there in list1')

# combine list1 and list2
c1.update(list2)
print(sum(c1.values()), 'no. of alphabets are there in list1')

# Print 3 highest occuring alphabets
print(c1.most_common(3), '3 most commonly occuring alphabets in decreasing \
order of frequency')

# Now subtract list 2 from list 1
c1.subtract(list2)
print(sum(c1.values()))

# Intersection of 2 counters
print(c1 & c2)
