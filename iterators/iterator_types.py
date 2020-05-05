'''
There are many iterating techniques provided by Python.
Below are the examples with their usage
'''
weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
weekdays_kannada = ['bha', 'som', 'man', 'bud', 'gur', 'shu', 'sha']

#Simple looping techniques
print('Iterating using for loop')
for weekday in weekdays:
    print(weekday)

#Iter can be used with next() until it reaches end
print('Iterating using iter')
i = iter(weekdays)
print(next(i))
print(next(i))

#Use when index is also required
print('Iterating using enumerate')
for day, weekday in enumerate(weekdays, start=1):
    print(day, weekday)

#To be used when iterating 2 objects same time
print('Iterate 2 lists at same time')
for day,weekday in enumerate(zip(weekdays, weekdays_kannada), start=1):
    print(day, weekday[0],'=',weekday[1], 'in Kannada')
