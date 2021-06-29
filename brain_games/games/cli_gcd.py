#!/usr/bin/env python3

import prompt
import random
from brain_games.games.engine import is_gcd
from brain_games.games.engine import welcome_user
from brain_games.games.engine import uncor


def gcd():
    welcome_user()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Find the greatest common divisor of given numbers.')

    i = 0
    while i <= 2:
        num_1 = random.randint(1, 99)
        num_2 = random.randint(1, 99)
        print('Question: {} {}'.format(num_1, num_2))
        ans = prompt.integer('Your answer: ')
        cor_ans = is_gcd(num_1, num_2)
        if ans == cor_ans:
            print('Correct!')
            i += 1
        elif ans != cor_ans:
            unc = uncor(ans, cor_ans, name)
            return unc
    print('Congratulations, {}!'.format(name))
