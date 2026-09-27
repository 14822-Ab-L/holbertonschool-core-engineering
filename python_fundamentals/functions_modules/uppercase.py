#!/usr/bin/env python3

def uppercase(str):
    result = ""

    for character in str:
        ascii_value = ord(character)

        if ord('a') <= ascii_value <= ord('z'):
            ascii_value = ascii_value - 32
            character = chr(ascii_value)

        result += character

    print("{}".format(result))
