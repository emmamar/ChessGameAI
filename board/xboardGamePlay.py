from Board import Board
from Player import Player
from Move import Move
import copy

'''this class starts the game on the computer. It creates a board 
object and can create 2 players, determine the next move for the 
computer player and play the move for the human player in turn.'''

'''constructor: creates a board object'''
class xboardGamePlay:
  def __init__ (self):
    self.board_object = Board()
    self.white_turn = True

  '''start the game by creating 2 players'''
  def start_new_game(self):
    self.player1_computer = Player("B", 2)
    self.player2_human = Player("W", 0)
    

  '''determine and play the computers move'''
  def play_move_computer(self):
    if not self.white_turn:
      p1next, heur = self.player1_computer.determineNextMove(
        self.board_object, None
      )
      self.board_object.try_move_piece(p1next)
      self.board_object.save_board()
      self.white_turn = True
      return p1next
    else:
      '''isnt blacks turn'''
      return None
    

  '''play the human players move on the board'''
  def play_move_human(self, given_move):
    if self.white_turn:
      can_move_piece = self.board_object.try_move_piece(given_move)
      self.board_object.save_board()
      self.white_turn = False
      return can_move_piece
    else:
      '''illegal move or isnt whites turn'''
      return False 


          
 
