#!/usr/bin/env python3

import prompt
import random


def print_description():
    print('Find the greatest common divisor of given numbers.')


def ask_question():
    number_1 = random.randint(1, 99)
    number_2 = random.randint(1, 99)
    number = number_1, number_2
    question = 'Question: {} {}'.format(number_1, number_2)
    return number, question


def is_answer_correct(number):
    number_1 = number[0]
    number_2 = number[1]
    while number_1 != number_2:
        if number_1 > number_2:
            number_1 = number_1 - number_2
        else:
            number_2 = number_2 - number_1
    return number_2


def get_answer():
    return prompt.integer('Your answer: ')


def is_incorrect_answer(answer, name, number):
    return """'{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!""".format(answer, is_answer_correct(number), name)
