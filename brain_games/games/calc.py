#!/usr/bin/env python3

import random


DESCRIPTION = 'What is the result of the expression?'
FIRST, END = 1, 11


def ask_question():
    number_1 = random.randint(FIRST, END)
    number_2 = random.randint(FIRST, END)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    return number_1, number_2, operator


def get_question_and_correct_answer():
    number_1, number_2, operator = ask_question()
    add = number_1 + number_2
    sub = number_1 - number_2
    mul = number_1 * number_2
    if add and operator == '+':
        result = add
    elif sub and operator == '-':
        result = sub
    elif sub == 0 and operator == '-':
        result = sub
    elif mul and operator == '*':
        result = mul
    question = '{} {} {}'.format(str(number_1), operator, str(number_2))
    return str(result), question
