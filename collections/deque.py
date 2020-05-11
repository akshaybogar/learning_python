from collections import deque
import string

# Deque is a double ended queue. THe below is an example of deque object
# containing lowercase ascii letters
d = deque(string.ascii_lowercase)
print(d)

# To remove elements from end of the deque use pop()
d.pop()

# Use pop_left() to remove elements from beginning of the deque
d.popleft()

#Use append to add elements to end of the deque
d.append(26)

#Use append_left to insert elements in the beginnning
d.appendleft(1)

print(d)

# To right rotate the deque use rotate(no. of items) defaults to 1
d.rotate(5)
print(d)

# To left rotate deque use negative index
d.rotate(-5)
print(d)
