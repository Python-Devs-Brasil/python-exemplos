from guess import *

guess = Guess()
guess.rangeStart  = 1
guess.rangeEnd    = 20
guess.maxAttempts = 6
guess.number = guess.getRand(guess.rangeStart, guess.rangeEnd)

print('Hello! What is your name?')
player = Player(raw_input())

print('Well, ' + player.name + ', I am thinking of a number between ' +
str(guess.rangeStart) + ' and ' + str(guess.rangeEnd) + '.')

while guess.taken < guess.maxAttempts:
    print('Take a guess.')
    player.guess = int(raw_input())
    guess.setTaken()
    if guess.guessIsTooLow(player.guess):
        print('Your guess is too low.')
    if guess.guessIsTooHigh(player.guess):
        print('Your guess is too high.')
    if guess.guessIsOk(player.guess):
        break

if guess.guessIsOk(player.guess):
    print('Good job, ' + player.name + '! You guessed my number in ' +
    str(guess.taken) + ' guesses!')
else:
    print('Nope. The target I was thinking of was ' + str(guess.number))
