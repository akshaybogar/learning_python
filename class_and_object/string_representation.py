class Person:
    def __init__(self):
        self.fname = 'Akshay'
        self.lname = 'Bogar'
        self.age = 25

    # Usually used for debugging purposes
    def __repr__(self):
        return 'Firstname: {}, Lastname: {}, Age: {}'.format(self.fname,
        self.lname, self.age)

    def __str__(self):
        return '{} {} is {}'.format(self.fname, self.lname, self.age)

# All of the below will print <class '__main__.Person'> when __repr__ etc
#are not overridden
print(repr(Person()))
print(str(Person()))
