from Board import Board
from Player import Player
from Move import Move
import copy

def start_new_game();
    board_object = createBoard()
    player1_computer = Player("B")

def play_move(): 
    player1_next_move = player1_computer.determineNextMove(copy.deepcopy(board_object))
    board_object.move_piece(player2_next_move) 

def save_board():
    board_object.save_board() 

def createBoard():
    f = open('Board.txt')
    board_object = Board(f)
    return board_object 
          
~      
