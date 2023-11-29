#!/usr/bin/python3
def uppercase(str):
    for char in str:
        uni_code = ord(char)
        if 97 <= uni_code <= 122:
            uni_code -= 32
            print("{}".format(chr(uni_code)), end='')
            print()
