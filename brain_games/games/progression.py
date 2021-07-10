#!/usr/bin/env python3

import prompt
import random


def print_description():
    print('What number is missing in the progression?')


def get_progression():
    number_1 = random.randint(1, 9)
    number_2 = random.randint(1, 9)
    count = random.randint(2, 6)
    i = 0
    result = ''
    while i <= 9:
        number_1 += count
        if i != number_2:
            result += ' ' + str(number_1)
        elif i == number_2:
            correct_answer = number_1
            result += ' ' + '..'
        i += 1
    return correct_answer, result[1:]


def ask_question():
    number, progression = get_progression()
    question = 'Question: {}'.format(progression)
    return number, question


def is_answer_correct(number):
    return number


def get_answer():
    return prompt.integer('Your answer: ')


def is_incorrect_answer(answer, name, number):
    correct_answer = is_answer_correct(number)
    return """'{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!""".format(answer, correct_answer, name)
