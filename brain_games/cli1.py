import prompt
import random


def is_even():
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0

    while i <= 2:
        rand = random.randint(1, 99)
        print('Question: {}'.format(rand))
        ans = prompt.string('Answer: ')
        if rand % 2 == 0 and ans == 'yes' or rand % 2 == 1 and ans == 'no':
            print('Correct!')
            i += 1
        else:
            if rand % 2 == 0 and ans != 'yes':
                wrong = print("""'{}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {}!""".format(ans, name))
            elif rand % 2 == 1 and ans != 'no':
                wrong = print("""'{}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {}!""".format(ans, name))
            return wrong
    print("Congratulations, {}!!!".format(name))
