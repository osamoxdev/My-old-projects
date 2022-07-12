# game methodes
# creat the game board
from player import HumenPlayer, CoputerPlayer
import time

class TicTacToe:
  def __init__(self):

    self.board = [' ' for _ in range(9)] # a list for 3X3 spaces
    self.current_winner = None # who is the winner

  def dsign_board(self):

    for row in [self.board[i*3:(i+1)*3]for i in range(3)]:

      print('|'+'|'.join(row)+'|')

  @staticmethod
  def board_number(): # one number for ech space
    numbers = [[str(i) for i in range(j*3, (j+1)*3)]for j in range(3)]

    for row in numbers:
      print('|'+'|'.join(row)+'|')
      


  def avalibale_move(self):

    return [i for i, spot in enumerate(self.board) if spot == ' ']
    # move = []

    # for (i, spot) in enumerate(self.board):
    # # enumerate the spot to i
    #   if spot == ' ' :
    #     move.append(i)

    # return move
  def empety_square(self) :

    return ' ' in self.board
  
  def empety_squares_num(self) :

    return self.board.count(' ')

  def make_move(self, square, letter):

   if self.board[square] == ' ' :
     self.board[square] = letter
     if self.winner(square, letter):                                            
       self.current_winner = letter
     return True
   return False 

  def winner(self, square, letter) :
    # winner if 3 in a raw
    # check rew index
    row_index = square // 3
    row = self.board[row_index*3: (row_index + 1)*3]
    if all([spot == letter for spot in row]) :
      return True

    #Check column
    col_index = square % 3
    col = [self.board[col_index+i*3 ]for i in range(3)]
    if all([spot == letter for spot in col]) :
      return True
    
    if square %2 == 0 :
      #Check diagonals
      # diagonals come for only even numbers(0, 2, 4, 6, 8)

      diagonal1 = [self.board[i] for i in [0, 4, 8]]
      if all([spot == letter for spot in diagonal1]) :
        return True

      diagonal2 = [self.board[i] for i in [2, 4, 6]]
      if all([spot == letter for spot in diagonal2]) :
        return True

    return False
    




# we're using "game" becuase we're out side the class
def paly(game, Xplayer, Oplayer, start_game=True) :

  if start_game :
    game.board_number()

  letter = 'X' #starting letter

  while game.empety_square():

    if letter == 'O' :

      square = Oplayer.move(game)

    else :

      square = Xplayer.move(game)


    if game.make_move(square, letter) :
      if start_game:
        print(letter + f' makes a move to square {square}')
        game.dsign_board()
        print('\n')

      if game.current_winner: # winner != none wich mean there is a winner

        if start_game :
          print(letter + ' wins!')
        return letter

      #alternate letter
      letter = 'O' if letter == 'X' else 'X'
      # if letter == 'X' :
      #   letter = 'O'
    time.sleep(1)
      # else :
      #   letter = 'X'
  if start_game:

    print('it\'s a tie!')

 
if __name__  == '__main__' :

  Xplayer = CoputerPlayer ('X')
  Oplayer = HumenPlayer('O')
  t = TicTacToe()
  paly(t, Xplayer, Oplayer, start_game=True)
