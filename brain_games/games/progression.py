#!/usr/bin/env python3

import random


DESCRIPTION = 'What number is missing in the progression?'
FIRST, END = 1, 8
DIF_FIRST, DIF_END = 0, 7

def get_progression():
    number = random.randint(FIRST, END)
    difference = random.randint(DIF_FIRST, DIF_END)
    i = 0
    result = [number]
    while i <= END:
        number += difference
        result += [number]
        i += 1
    return result


def get_question_and_correct_answer():
    progression = get_progression()
    empty_index = random.randint(FIRST, END)
    i = 0
    result = ''
    while i < len(progression) - 1:
        if i != empty_index:
            result += ' ' + str(progression[i])
            i += 1
        elif i == empty_index:
            skip_number = str(progression[i])
            result += ' ' + '..'
            i += 1
    return skip_number, result[1:]
