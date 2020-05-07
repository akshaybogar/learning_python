def addition(*args):
    '''
    Takes variable number of arguments and returns sum of all the srguments.
    '''
    result = 0
    for arg in args:
        result += arg
    return result

#Below prints the output as 10
print(addition(1,2,3,4))
#Include * with list /tuple if being passed as arguments
nums_list = [1,2,3,4,5,6,7,8,9]
print(addition(*nums_list))
