#!/usr/bin/env python3

def welcome_user():
    print('Welcome to the Brain Games!')


def is_gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b

def uncor(a, b, c):
    print("""'{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!""".format(a, b, c))