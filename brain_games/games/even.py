#!/usr/bin/env python3

import random


DESCRIPTION = 'Answer "yes" if given number is even, otherwise answer "no".'

FIRST, END = 1, 100


def get_question():
    number = random.randint(FIRST, END)
    return number


def is_even(number):
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def get_round():
    number = get_question()
    correct_answer = is_even(number)
    return correct_answer, str(number)
