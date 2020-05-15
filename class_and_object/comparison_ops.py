class Employee():
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def __gt__(self, other):
        return self.experience > other. experience

    def __ge__(self, other):
        return self.experience >= other. experience

    def __lt__(self, other):
        return self.experience < other.experience

    def __le__(self, other):
        return self.experience <= other.experience

if __name__ == '__main__':
    cricketers = []
    cricketers.append(Employee('Rohit', 12))
    cricketers.append(Employee('Virat', 8))
    cricketers.append(Employee('MS', 15))
    cricketers.append(Employee('Sachin', 20))


    # Compares 2 employees based on years of experience
    print(cricketers[0] > cricketers[1])

    # Sort the objects
    sorted_list = sorted(cricketers)
    for i in sorted_list:
        print(i.name)
