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
        correct_answer = 'no'
        return correct_answer
    while i < number:
        if number % i != 0:
            i += 1
        else:
            correct_answer = 'no'
            return correct_answer
    correct_answer = 'yes'
    return correct_answer


def get_round():
    number = get_question()
    correct_answer = is_prime(number)
    return correct_answer, str(number)
