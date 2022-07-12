# 3 classes for (player class: the parent class
# HumenPlayer and CoputerPlayer chailed classes)

# every class has a move function

import math
import random


class Player:
  def __init__(self, letter) :
    self.letter = letter # X & O


  def move(self, game) :

    pass


class CoputerPlayer(Player):
  def __init__(self, letter) :
    super().__init__(letter)


  def move(self, game):

    square = random.choice(game.avalibale_move())
    return square

class HumenPlayer(Player):
  def __init__(self, letter) :
    super().__init__(letter)


  def move(self, game):

    valid_square = False

    valu = None

    while valid_square == False :

      square = input(f'{self.letter}\'s turn chosse your move (0-8) : ')
      try :

        valu = int(square)

        if valu not in game.avalibale_move() :

          raise ValueError

        valid_square = True
      except ValueError:
          
        print('Invalid squer chosse again')

    return valu


