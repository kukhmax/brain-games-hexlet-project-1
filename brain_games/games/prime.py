#!/usr/bin/env python3

import random
import prompt


def print_description():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def ask_question():
    number = random.randint(1, 100)
    question = 'Question: {}'.format(number)
    return number, question


def is_answer_correct(number):
    i = 2
    if number < 2:
        return 'no'
    while i < number:
        if number % i != 0:
            i += 1
        else:
            return 'no'
    return 'yes'


def get_answer():
    return prompt.string('Your answer: ')


def is_incorrect_answer(answer, name, number):
    correct_answer = is_answer_correct(number)
    return """'{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!""".format(answer, correct_answer, name)
