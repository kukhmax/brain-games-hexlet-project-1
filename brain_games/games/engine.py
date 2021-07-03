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
        return result[1:]


def is_prime(a):
    i = 2
    if a < 2:
        return 'no'
    while i < a:
        b = a % i
        if b != 0:
            i += 1
        else:
            return 'no'
    return 'yes'


def is_calc_answer_incorrect(ans, add, sub, mul, operator, name):
    if ans != add and operator == '+':
        return is_answer_incorrect(ans, add, name)
    elif ans != sub and operator == '-':
        return is_answer_incorrect(ans, sub, name)
    elif ans != mul and operator == '*':
        return is_answer_incorrect(ans, mul, name)


def is_answer_incorrect(a, b, c):
    print("""'{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!""".format(a, b, c))


def congratulations(a):
    print('Congratulations, {}!'.format(a))
