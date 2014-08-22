import unittest

class Guess:
    taken = 0

    def getRand(self, start, end):
        from random import randint
        return randint(start, end)

    def setTaken(self):
        self.taken += 1

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



if __name__ == '__main__':
    unittest.main()
