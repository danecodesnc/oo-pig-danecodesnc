from random import choice

#No tests are written in this homework. 
#There is only one dice being used for this game, not two.

SIDES = [1, 2, 3, 4, 5, 6,]

# def roll():
#     return random.choice([1,2,3,4,5,6])

class Game:
    def __init__(self,):
        self.player = Player("Dane")
        self.computer = Computer("Computer")
        self.dice = Dice(SIDES)

    
    def round(self):
        # turnscore = 0
        player_turn_score = 0
        computer_turn_score = 0
       
  
        while self.player.score < 100 and self.computer.score < 100:
            choice = input ("Would you like to (r)oll or (s)top? ")
            if choice == 'r':
                roll = self.dice.roll()
                player_turn_score += roll
            else:
                self.player.score += player_turn_score
                while computer_turn_score < 20:
                    roll = self.dice.roll()
                    computer_turn_score += roll
                self.computer.score += computer_turn_score
                print(f'player score{self.player.score}, computer score{self.computer.score}')
                

class Dice:
        def __init__(self, sides):
            self.sides = sides

        def roll(self):
            score = choice(self.sides) 
            return score

            # When your setting up your dice class. This will give a random instance of 1 - 6. 
            # Would you generate a new instance of the dice class?
            # Dice has 6 sides.
            # You have 1 dice and you can perform an action on that dice that will roll itself.
            # Create the dice with the options and perform the actions. 
            
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    def __str__(self):
            return f"{self.name}"
      

class Computer:
    # In this case this will be a computer generated option, rather than it be another human player.
        def __init__(self, name):
            self.name = name
            self.score = 0

        def __str__(self):
            return f"{self.name}"

        


game = Game()
game.round()

