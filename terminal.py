#!/usr/bin/env python3

# Libraries
from base64 import b64encode, b64decode

# Messages
warn = '!!!!!!!!!!!!!!!!!!!!!!!! WARNING: '
valid = '\nPlease Enter a Valid Entry!\n'

# Menu/Encode/Decode Logic
def app(st):

    if st == '1':
        code = input('Enter Stuff to Encode: ').encode()
        print('\n')
        try:
            ans = b64encode(code)
            print('\n',str(ans)[2:-1],'\n')
            return
        except Exception as x:
            print(warn,x,'\n')
    elif st == '2':
        code = input('Enter Stuff to Decode: ').encode()
        print('\n')
        try:
            ans = b64decode(code)
            print('\n',str(ans)[2:-1],'\n')
            return
        except Exception as x:
            print(warn,x,'\n')
    elif st == 'q':
        exit()
    else:
        print(valid)
        return

#Main Menu Loop
while True:
	try:    
		app(input('\nEnter 1 to Encode\n\nEnter 2 to Decode\n\nEnter q to Quit\n'))
	except KeyboardInterrupt:
		break
