from Board import Board
from Player import Player
from Move import Move
import copy

class xboardGamePlay:
  def __init__ (self):
    self.board_object = Board()

  def start_new_game(self):
    self.player1_computer = Player("B", "computer")
    self.player2_human = Player("W", "human")
    
  def play_move_computer(self):
    p1nm=self.player1_computer.determineNextMove(copy.deepcopy(self.board_object))
    self.board_object.move_piece(p1nm)
    self.save_board()
    return p1nm

  def play_move_human(self, given_move_alg):
    move_from_alg_dic={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    split = list(given_move_alg)
    human_move = (Move(int(split[1]) - 1, 
    move_from_alg_dic[split[0]], int(split[3]) -1, 
    move_from_alg_dic[split[2]]))
    self.board_object.move_piece(human_move)
    self.save_board
 
  def save_board(self):
    self.board_object.save_board() 

          
 
