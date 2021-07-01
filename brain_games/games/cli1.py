import prompt
import random
from brain_games.games.engine import welcome_user
from brain_games.games.engine import incor
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
        rand = random.randint(1, 99)
        print('Question: {}'.format(rand))
        ans = prompt.string('Answer: ')
        if rand % 2 == 0 and ans == 'yes' or rand % 2 == 1 and ans == 'no':
            print('Correct!')
            i += 1
        else:
            if rand % 2 == 0 and ans != 'yes':
                wrong = incor(ans, yes, name)
            elif rand % 2 == 1 and ans != 'no':
                wrong = incor(ans, no, name)
            return wrong
    congratulations(name)
