#!/usr/bin/env python3

import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
FIRST, END = 1, 100


def get_question_and_correct_answer():
    number = random.randint(FIRST, END)
    i = 2
    if number < 2:
        return 'no', str(number)
    while i < number:
        if number % i != 0:
            i += 1
        else:
            return 'no', str(number)
    return 'yes', str(number)
