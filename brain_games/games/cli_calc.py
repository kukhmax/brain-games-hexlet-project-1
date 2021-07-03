#!/usr/bin/env python3

import prompt
import random
from brain_games.games.engine import welcome_user
from brain_games.games.engine import is_answer_incorrect
from brain_games.games.engine import congratulations


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
        elif ans == sub and operator == '-':
            print('Correct!')
        elif ans == mul and operator == '*':
            print('Correct!')
            i += 1
        else:
            if ans != add and operator == '+':
                return is_answer_incorrect(ans, add, name)
            elif ans != sub and operator == '-':
                return is_answer_incorrect(ans, sub, name)
            elif ans != mul and operator == '*':
                return is_answer_incorrect(ans, mul, name)
    congratulations(name)
