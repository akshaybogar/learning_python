'''
Program to find gcd of two numbers
'''

def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % a
    return a

if __name__ == '__main__':
    print(gcd(10,20)) # ans 10
    print(gcd(12, 8)) # ans 4
