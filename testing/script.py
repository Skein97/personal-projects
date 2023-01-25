import random


def run_guess(guess, answer):
    try:
        if 0 < int(guess) < 11:
            if int(guess) == answer:
                print('You are right!')
                return True
        else:
            print('From 1 to 10')
            return False
    except ValueError:
        print('Please enter a number')
        return False


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while 1:
        guess = input('Guess a number 1 - 10: ')
        if run_guess(guess, answer):
            break

