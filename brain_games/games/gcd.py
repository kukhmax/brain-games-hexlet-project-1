#!/usr/bin/env python3

import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
FIRST, END = 1, 100


def get_question():
    number_1 = random.randint(FIRST, END)
    number_2 = random.randint(FIRST, END)
    return number_1, number_2


def calculate_gcd(number_1, number_2):
    while number_1 != number_2:
        if number_1 > number_2:
            number_1 = number_1 - number_2
        else:
            number_2 = number_2 - number_1
    return number_2


def get_round():
    number_1, number_2 = get_question()
    question = str(number_1) + ' ' + str(number_2)
    number_2 = calculate_gcd(number_1, number_2)
    return str(number_2), question
