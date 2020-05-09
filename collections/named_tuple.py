'''
Program to show how to use namedtuple
'''
import collections

#Create a named tuple Point with name Point which takes 2 parameters x and y
Point = collections.namedtuple('Point', 'x y')
p1 = Point(10, 20)
print(p1)

#Use parameters like below instead of positional parameters
print(p1.x, p1.y)

#To create a new instance i.e by changing a parameter value
p1 = p1._replace(x=100)
print(p1)
