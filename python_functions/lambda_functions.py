def return_squares(x):
    return x**2

nums_list = [1, 2, 3, 4, 5]

#Using map to convert all numbers in the list to squares
print(list(map(return_squares, nums_list)))

#The same can be achieved using lambda functions without adding complexity and
#hence making code more readable
print(list(map(lambda x: x**2, nums_list)))
