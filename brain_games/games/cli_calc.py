#!/usr/bin/env python3

import prompt
import random
from brain_games.games.engine import welcome_user
from brain_games.games.engine import congratulations
from brain_games.games.engine import is_calc_answer_incorrect


def get_result_of_calc():
    welcome_user()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
    i = 0

    while i <= 2:
        num_1 = random.randint(1, 11)
        num_2 = random.randint(1, 11)
        mylist = ['+', '-', '*']
        operator = random.choice(mylist)
        add = num_1 + num_2
        sub = num_1 - num_2
        mul = num_1 * num_2
        print('Question: {} {} {}'.format(num_1, operator, num_2))
        ans = prompt.integer('Your answer: ')
        if ans == add and operator == '+':
            print('Correct!')
            i += 1
        elif ans == sub and operator == '-':
            print('Correct!')
            i += 1
        elif ans == mul and operator == '*':
            print('Correct!')
            i += 1
        else:
            return is_calc_answer_incorrect(ans, add, sub, mul, operator, name)
    congratulations(name)
