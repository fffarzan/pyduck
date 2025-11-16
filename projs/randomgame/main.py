from sys import argv
from random import randint

answer = randint(int(argv[1]), int(argv[2]))

def run():
    while True:
        try:
            guess = int(input(f'guess a number between {argv[1]}~{argv[2]}: '))
            if (int(argv[1]) - 1) < guess < (int(argv[2]) + 1):
                if guess == answer:
                    print(f'guess: {guess}, answer: {answer}. done!')
                    break
                else:
                    print('try one more time!')
            else:
                print('err: just number between given range accepted')
        except ValueError:
            print('err: just number accepted')
            continue

run()
