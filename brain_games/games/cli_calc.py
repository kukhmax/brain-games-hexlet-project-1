#!/usr/bin/env python3

import prompt
import random


def calc():
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
    i = 0

    while i <= 2:
        num_1 = random.randint(1, 15)
        num_2 = random.randint(1, 10)
        mylist = ['+', '-', '*']
        sing = random.choice(mylist)
        add = num_1 + num_2
        sub = num_1 - num_2
        mul = num_1 * num_2
        print('Question: {} {} {}'.format(num_1, sing, num_2))
        ans = prompt.integer('Your answer: ')
        if ans == add or ans == sub or ans == mul:
            print('Correct!')
            i += 1
        else:
            if ans != add and sing == '+':
                result = print("""'{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!""".format(ans, add, name))
            elif ans != sub and sing == '-':
                result = print("""'{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!""".format(ans, sub, name))
            elif ans != mul and sing == '*':
                result = print("""'{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!""".format(ans, mul, name))
            return result
    print('Congratulations, {}!'.format(name))