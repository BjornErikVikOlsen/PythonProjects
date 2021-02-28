import random

def guess(x):
    randomNumber = random.randint(1,x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < randomNumber:
            print('To low. Guess again')
        elif guess > randomNumber:
            print('To high. Guess again')

    print(f'You have guessed the number {randomNumber}')

def computerGuess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)').lower
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Computer guessed your number {guess} correctly') 