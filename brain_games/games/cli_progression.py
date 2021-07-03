#!/usr/bin/env python3

import prompt
import random
from brain_games.games.engine import welcome_user
from brain_games.games.engine import progression
from brain_games.games.engine import is_answer_incorrect
from brain_games.games.engine import congratulations


def get_missing_number_in_progression():
    welcome_user()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What number is missing in the progression?')
    i = 0

    while i < 3:
        num = random.randint(1, 9)
        num_1 = random.randint(0, 9)
        count = random.randint(2, 6)
        prog = progression(num, count, num_1, 2)
        print('Question: {}'.format(prog))
        ans = prompt.integer('Your answer: ')
        cor_ans = progression(num, count, num_1, 1)
        if ans == cor_ans:
            print('Correct!')
            i += 1
        elif ans != cor_ans:
            return is_answer_incorrect(ans, cor_ans, name)
    congratulations(name)
