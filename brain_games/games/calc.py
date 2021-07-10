#!/usr/bin/env python3

import prompt
import random


def print_description():
    print('What is the result of the expression?')


def ask_question():
    number_1 = random.randint(1, 11)
    number_2 = random.randint(1, 11)
    mylist = ['+', '-', '*']
    operator = random.choice(mylist)
    number = number_1, number_2, operator
    question = 'Question: {} {} {}'.format(number_1, operator, number_2)
    return number, question


def is_answer_correct(number):
    number_1 = number[0]
    number_2 = number[1]
    operator = number[2]
    add = number_1 + number_2
    sub = number_1 - number_2
    mul = number_1 * number_2
    if add and operator == '+':
        return add
    elif sub and operator == '-':
        return sub
    elif mul and operator == '*':
        return mul


def get_answer():
    return prompt.integer('Your answer: ')


def is_incorrect_answer(answer, name, number):
    correct_answer = is_answer_correct(number)
    return """'{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!""".format(answer, correct_answer, name)
