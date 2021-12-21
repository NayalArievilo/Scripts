from random import randint
import sys

try:
    def game():
        while True:
            num = randint(int(sys.argv[1]), int(sys.argv[2]))
            try:
                guess = int(input(
                    f'\nGuess a number from {sys.argv[1]} to {sys.argv[2]}: '))
                if guess == num:
                    print(f'\nCorret, the number was {num}\n')
                    break
                if guess != num:
                    print(f'\nIncorrect, the number was {num}\n')
                if guess < int(sys.argv[1]) or guess > int(sys.argv[2]):
                    print(
                        f'\nI said {sys.argv[1]} to {sys.argv[2]}, try again\n')
                else:
                    continue
            except ValueError:
                print('\n' 'I said \"NUMBERS\"\n')
            continue
except AttributeError as er:
    raise er

game()
