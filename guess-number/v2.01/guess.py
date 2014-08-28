import unittest

class Guess:
    taken = 0

    def getRand(self, start, end):
        from random import randint
        return randint(start, end)

    def setTaken(self):
        self.taken += 1

    def guessIsTooLow(self, playerGuess):
        if playerGuess < self.number:
            return True
        else:
            return False

    def guessIsTooHigh(self, playerGuess):
        if playerGuess > self.number:
            return True
        else:
            return False

    def guessIsOk(self, playerGuess):
        if playerGuess == self.number:
            return True
        else:
            return False


class Player:
    guess = 0

    def __init__(self, name):
        self.name = name


class GuessTest(unittest.TestCase):

    def testRand(self):
        guess = Guess()
        guess.rangeStart = 1
        guess.rangeEnd   = 20
        randoNumber = guess.getRand(guess.rangeStart, guess.rangeEnd);
        # Como testar "getRand()" ? 

    def testSetTaken(self):
        guess = Guess()
        self.assertEqual(0, guess.taken)

        guess.setTaken()
        guess.setTaken()
        guess.setTaken()
        self.assertEqual(3, guess.taken)

#    def testRange(self):
#        guess = Guess()
#        guess.rangeStart = 1
#       guess.rangeEnd   = 20
#        self.assertEqual(1, guess.rangeStart)
#        self.assertEqual(20, guess.rangeEnd)

    def testGuessIsTooLow(self):
        player = Player("foo")

        guess = Guess()
        guess.number = 12
        
        player.guess = 8
        self.assertTrue(guess.guessIsTooLow(player.guess))

        player.guess = 16
        self.assertFalse(guess.guessIsTooLow(player.guess))

    def testGuessIsTooHigh(self):
        player = Player("foo")

        guess = Guess()
        guess.number = 12
        
        player.guess = 14
        self.assertTrue(guess.guessIsTooHigh(player.guess))

        player.guess = 10
        self.assertFalse(guess.guessIsTooHigh(player.guess))

    def testGuessIsOk(self):
        player = Player("foo")

        guess = Guess()
        guess.number = 12
        
        player.guess = 12
        self.assertTrue(guess.guessIsOk(player.guess))

        player.guess = 13
        self.assertFalse(guess.guessIsOk(player.guess))

if __name__ == '__main__':
    unittest.main()
