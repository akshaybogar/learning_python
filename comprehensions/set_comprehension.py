'''
Program to demonstrate working of set comprehension
'''

cel_temp = [12, 34, 53, 65, 12, 12, 45, 55, 53]

# Convert all celcius temperature to fahrenheit scale. Include unique temperature
fah_temp = {(f*9/5)+32 for f in cel_temp}
print(fah_temp)

# Convert all character to uppercase
s = 'Hi I am learning new concepts in Python'
uppercase_set = {u.upper() for u in s if not u.isspace()}
print(uppercase_set)
