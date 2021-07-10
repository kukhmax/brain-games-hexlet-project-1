#!/usr/bin/env python3

import random
import prompt


def print_description():
    print('Answer "yes" if given number is even, otherwise answer "no".')


def ask_question():
    number = random.randint(1, 100)
    question = 'Question: {}'.format(number)
    return number, question


def is_answer_correct(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_answer():
    return prompt.string('Your answer: ')


def is_incorrect_answer(answer, name, number):
    correct_answer = is_answer_correct(number)
    return """'{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!""".format(answer, correct_answer, name)
