#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    output = my_string.translate({ord(i): None for i in 'cC'})
    return output
