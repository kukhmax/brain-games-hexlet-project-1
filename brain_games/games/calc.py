#!/usr/bin/env python3

import random


DESCRIPTION = 'What is the result of the expression?'
FIRST, END = 1, 11


def get_question():
    number_1 = random.randint(FIRST, END)
    number_2 = random.randint(FIRST, END)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    return number_1, number_2, operator


def get_round():
    number_1, number_2, operator = get_question()
    add = number_1 + number_2
    sub = number_1 - number_2
    mul = number_1 * number_2
    if operator == '+':
        result = add
    elif operator == '-':
        result = sub
    elif operator == '*':
        result = mul
    question = f'{number_1} {operator} {number_2}'
    return str(result), question
