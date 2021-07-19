#!/usr/bin/env python3

import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
FIRST, END = 1, 100


def get_question():
    number = random.randint(FIRST, END)
    return number


def is_prime(number):
    i = 2
    if number < 2:
        return False
    while i < number:
        if number % i != 0:
            i += 1
        else:
            return False
    return True


def get_round():
    number = get_question()
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, str(number)
