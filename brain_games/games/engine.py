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


def progression(a, count, b, c):
    i = 0
    result = ''
    while i <= 9:
        a += count
        if i != b:
            result += ' ' + str(a)
        elif i == b:
            ans = a
            result += ' ' + '..'
        i += 1
    if c == 1:
        return ans
    else:
        return result


def uncor(a, b, c):
    print("""'{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!""".format(a, b, c))


def congratulations(a):
    print('Congratulations, {}!'.format(a))
