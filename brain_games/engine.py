#!/usr/bin/env python3

import prompt


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))

    game.print_description()

    i = 0
    while i < 3:
        number, question = game.ask_question()
        print(question)

        answer = game.get_answer()
        if answer == game.is_answer_correct(number):
            print('Correct!')
            i += 1
        else:
            return print(game.is_incorrect_answer(answer, name, number))
    print('Congratulations, {}!'.format(name))
