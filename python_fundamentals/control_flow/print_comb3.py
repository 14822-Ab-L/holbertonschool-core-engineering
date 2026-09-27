#!/usr/bin/env python3

for first in range(10):
    for second in range(first + 1, 10):
        if first == 8 and second == 9:
            print("{a}{b}".format(a=first, b=second))
        else:
            print("{a}{b}, ".format(a=first, b=second), end="")
