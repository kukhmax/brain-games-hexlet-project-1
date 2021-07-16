#!/usr/bin/env python3

import random


DESCRIPTION = 'What number is missing in the progression?'
FIRST, END = 1, 8
DIF_FIRST, DIF_END = 1, 7


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


def get_stirng_progression(progression, hole_index):
    i = 0
    result = ''
    while i < len(progression) - 1:
        if i != hole_index:
            result += ' ' + str(progression[i])
            i += 1
        elif i == hole_index:
            result += ' ' + '..'
            i += 1
    skip_number = str(progression[hole_index])
    return skip_number, result[1:]


def get_round():
    progression = get_progression()
    empty_index = random.randint(FIRST, END)
    correct_answer, question = get_stirng_progression(progression, empty_index)
    return correct_answer, question
