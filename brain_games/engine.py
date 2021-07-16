#!/usr/bin/env python3

import prompt

COUNT = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.DESCRIPTION)

    for i in range(COUNT):
        correct_answer, question = game.get_round()
        print(f'Question: {question}')

        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        elif answer != correct_answer:
            return print(f"""'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
    print(f'Congratulations, {name}!')
