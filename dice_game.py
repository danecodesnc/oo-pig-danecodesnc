import random

#No tests are written in this homework. 
#There is only one dice being used for this game, not two.

# SIDES = [1, 2, 3, 4, 5, 6,]

def roll():
    return random.choice([1,2,3,4,5,6])

class Game:
    def __init__(self,):
        self.player = Player("Dane")
        self.dealer = Dealer("Computer")
        self.dice = Dice()

    def deal_dice(self, role):
        if role == self.player:
            self.player.hand.append(self.dice())
        if role == self.computer:
            self.computer.hand.append(self.dice())
    
    def round(self):
        turnscore = 0
        self.dice.roll()
        while self.player.score < 100 and self.computer.score < 100:
            choice = input ("Would you like to (r)oll or (s)top? ")
            if choice == 'r':
                self.roll_dice(self.player)
                self.player.sum_score()
                self.computer.sum_score()
                if self.comptuer.score < 100:
                self.compute_one_roll(self.computer)
                print(f'Computer has {self.computer.score}')

            if self.player.score == 100:
                print(f'Winner!')
                return
            elif self.player.score == 1:
                print(f'You got a pig, no points granted for this turn, computer turn to play. {self.player.score}')
            



class Dice:
        def __init__(self, sides):
            self.sides = sides

        def roll(self):
            self.dice = sample(self.dice, len(self.dice))    
            # When your setting up your dice class. This will give a random instance of 1 - 6. 
            # Would you generate a new instance of the dice class?
            # Dice has 6 sides.
            # You have 1 dice and you can perform an action on that dice that will roll itself.
            # Create the dice with the options and perform the actions. 
            
class Player:
    def__init__(self, name):
        self.name = name
        self.score = 0
        
    def __str__(self):
            return f"{self.name}"

    def sum_hand(self):
        self.score = 0
        for dice in self.hand:
        if dice.side in range(1, 6):
            self.side += dice.side
        else:
            self.score += FACE_VALUES[dice.side]
        

class Computer:
    # In this case this will be a computer generated option, rather than it be another human player.
        def__init__(self, name):
        self.name = name
        self.score = 0

        def __str__(self):
            return f"{self.name}"

        def sum_hand(self):
            self.score = 0
            for dice in self.hand:
            if dice.side in range(1, 6):
                self.side += dice.side
            else:
                self.score += FACE_VALUES[dice.side]
        


game = Game()
game.round()

