def add_numbers(param1, param2, *, ignore_errors=False):
    return(param1 + param2)

#Use keyword arguments fro better readability
#Uncommenting below line will give error
#print(add_numbers(1, 2, 3))

print(add_numbers(1, 2, ignore_errors=True))
