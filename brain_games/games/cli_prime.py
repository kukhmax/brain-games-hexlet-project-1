#!/usr/bin/env python3

import prompt
import random
from brain_games.games.engine import welcome_user
from brain_games.games.engine import is_prime
from brain_games.games.engine import is_answer_incorrect
from brain_games.games.engine import congratulations


def is_number_prime():
    welcome_user()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0

    while i < 3:
        num = random.randint(1, 100)
        print('Question: {}'.format(num))
        ans = prompt.string('Your answer: ')
        cor_ans = prime(num)
        if ans == 'yes' and cor_ans == 'yes' or ans == 'no' and cor_ans == 'no':
            print('Correct!')
            i += 1
        else:
            n = 'no'
            y = 'yes'
            if ans != 'no' and cor_ans == 'no':
                wrong = is_answer_incorrect(ans, n, name)
            elif ans != 'yes' and cor_ans == 'yes':
                wrong = is_answer_incorrect(ans, y, name)
            return wrong
    congratulations(name)
