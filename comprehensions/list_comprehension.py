'''
Program to demonstrate working of list comprehension
'''

nums = [1,2,3,4,5,6,7,8,9,10]

# Print square of each number less than 8 the old way
nums_squared = list(map(lambda x: x**2, filter(lambda i: i<8, nums)))
print(nums_squared)

# Above can be easily achieved using list comprehension
nums_cubed = [i**3 for i in nums if i<8]
print(nums_cubed)
