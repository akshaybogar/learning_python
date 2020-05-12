'''
Program to demonstrate working of dictionary comprehension
'''

temp_celcius = [0, 22, 45, 65, 100]

# Create celcius to fahrenheit mapping using dictionary comprehension
cel_fah = {t: (t*9/5)+32 for t in temp_celcius}
print(cel_fah)

# Merge dictionaries into one using dictionary comprehension
t1 = {'john': 18, 'right': 19, 'rudolph': 21}
t2 = {'raina': 21, 'jade': 18}
new_team = {k:v for t in (t1, t2) for (k,v) in t.items()}
print(new_team)
