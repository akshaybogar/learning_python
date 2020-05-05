'''
This program demonstrates the use of string template.
String template is used for better readability and for reuse
'''


from string import Template

#Regular formatting
print('Hello World from {}'.format('Akshay'))

#Using template module in python
s = Template('Hello World from ${author}')
print(s.substitute(author='Akshay'))

#Data can also be passed using dictionary
print(s.substitute({"author":"Akshay"}))
