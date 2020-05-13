from enum import Enum, unique, auto

# Adding unique decorator makes sure that enum values are unique
@unique
class Fruits(Enum):
    APPLE = 1
    MANGO = 2
    GUAVA = 3
    # APPLE = 4 Uncommenting this line will throw error since duplicate names
    # are not allowed
    # GRAPE = 3 Uncommenting this line throws error since duplicate values
    # are not allowed because class Fruits is secorated with Fruits
    PINEAPPLE = auto() # Value is assigned automatically

# Print type of Fruit.APPLE
print(type(Fruits.APPLE))

#Print name and value of Fruits.APPLE
print(Fruits.APPLE.name, Fruits.APPLE.value)

print(Fruits.PINEAPPLE.value)
