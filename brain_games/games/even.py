#!/usr/bin/env python3

import random


DESCRIPTION = 'Answer "yes" if given number is even, otherwise answer "no".'

FIRST, END = 1, 100


def get_question_and_correct_answer():
    number = random.randint(FIRST, END)
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result, str(number)
