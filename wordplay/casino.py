import random

class Die(object):
    def __init__(self, maxNum):
        self.sides = maxNum

    def roll(self):
        return random.randint(1, self.sides)


d = Die(6)
d = Die(20)
print(d.roll())



class Deck(object):
    """docstring for Deck"""
    def __init__(self, arg):
        self.cards = []
        