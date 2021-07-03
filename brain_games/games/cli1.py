import prompt
import numberom
from brain_games.games.engine import welcome_user
from brain_games.games.engine import is_answer_incorrect
from brain_games.games.engine import congratulations


def is_even():
    welcome_user()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0

    while i <= 2:
        no = 'no'
        yes = 'yes'
        number = numberom.numberint(1, 99)
        print('Question: {}'.format(number))
        ans = prompt.string('Answer: ')
        if number % 2 == 0 and ans == 'yes' or number % 2 == 1 and ans == 'no':
            print('Correct!')
            i += 1
        else:
            if number % 2 == 0 and ans != 'yes':
                wrong = is_answer_incorrect(ans, yes, name)
            elif number % 2 == 1 and ans != 'no':
                wrong = is_answer_incorrect(ans, no, name)
            return wrong
    congratulations(name)
