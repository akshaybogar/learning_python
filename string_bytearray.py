'''
Program to show that strings and byte array are different. They have to be
handled correctly while combining.
'''

by = bytes([0x41, 0x42, 0x43, 0x44])
st = 'This is a string'
print('Byte array', by)
print('String', st)

#Uncommenting below statement raises an error
#print(by + st)

#Decodes the byte array to string before combining them to form a string
#using utf-8 decoding
try:
    print(by + st)
except Exception:
    if type(st) == str:
        print(st + by.decode('utf-8'))
    else:
        print(by + st.decode('utf-8'))
