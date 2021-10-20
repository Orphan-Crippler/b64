#!/usr/bin/env python3

from base64 import *

def app(st):

    if st == '1':
        print('Enter M to return to main menu\n')
        code = input('Enter Stuff to Encode: ').encode()
        if code.decode() == 'M':
            return
        print('\n')
        try:
            ans = b64encode(code)
            print('\n',str(ans)[2:-1],'\n')
            return
        except Exception as x:
            print('!!!!!!!!!!!!!!!!!!!!!!!! WARNING: ',x,'\n')
    elif st == '2':
        print('Enter M to return to main menu\n')
        code = input('Enter Stuff to Decode: ').encode()
        if code.decode() == 'M':
            return
        print('\n')
        try:
            ans = b64decode(code)
            print('\n',str(ans)[2:-1],'\n')
            return
        except Exception as x:
            print('!!!!!!!!!!!!!!!!!!!!!!!! WARNING: ',x,'\n')
    elif st == 'q':
        exit()
    else:
        print('\nPlease Enter a Valid Entry!\n')
        return

while True:
    app(input('\nEnter 1 to Encode\n\nEnter 2 to Decode\n\nEnter q to Quit\n'))
