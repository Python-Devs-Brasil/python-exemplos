import random

print('Hello! What is your name?')
myName = raw_input()
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

number = random.randint(1, 20)
guessesTaken = 0

while guessesTaken < 6:

    print('Take a guess.')
    guess = int(raw_input())
    guessesTaken = guessesTaken + 1
    
    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

if guess == number:
    print('Good job, ' + myName + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')

if guess != number:
    print('Nope. The number I was thinking of was ' + str(number))

