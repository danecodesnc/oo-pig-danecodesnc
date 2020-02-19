import random

#No tests are written in this homework. 

RANK = [1, 2, 3, 4, 5, 6,]


class Game:
    def __init__(self,):
        self.player = Player("Dane")
        self.dealer = Dealer("Computer")
        self.dice = Dice()
        self.score = {}


class Dice:
        def __init__(self, rank):
            self.rank = rank
            # When your setting up your dice class. This will give a random instance of 1 - 6. 
            # Would you generate a new instance of the dice class?
            # Dice has 6 sides.
            # You have 1 dice and you can perform an action on that dice that will roll itself.
            # Create the dice with the options and perform the actions. 
            #


class Player:
        def__init__(self):
        pass



class Dealer:
    # In this case this will be a computer generated option, rather than it be another human player.
        def__init__(self):
        pass

