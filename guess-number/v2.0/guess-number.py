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
    if player.guess < guess.number:
        print('Your guess is too low.')
    if player.guess > guess.number:
        print('Your guess is too high.')
    if player.guess == guess.number:
        break

if player.guess == guess.number:
    print('Good job, ' + player.name + '! You guessed my number in ' +
    str(guess.taken) + ' guesses!')

if player.guess != guess.number:
    print('Nope. The target I was thinking of was ' + str(guess.number))
