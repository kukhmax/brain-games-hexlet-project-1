#!/usr/bin/env python3

import prompt

COUNT = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))

    print(game.DESCRIPTION)

    i = 0
    while i < COUNT:
        correct_answer, question = game.get_question_and_correct_answer()
        print('Question: {}'.format(question))

        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            i += 1
        elif answer != correct_answer:
            return print("""'{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!""".format(answer, correct_answer, name))
    print('Congratulations, {}!'.format(name))
