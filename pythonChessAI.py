from Board import Board
from Player import Player
from Move import Move

def main():
    board_object = createBoard()
    player1_computer = Player("W")
    player2_computer = Player("B")
    ''' while not board_object.is_check_mate():'''
    for i in range(0,10):
        player1_next_move = player1_computer.determineNextMove(board_object)
        board_object.movePiece(player1_next_move)
        print board_object.toString()
        '''if not board_object.is_check_mate():'''
        player2_next_move = player2_computer.determineNextMove(board_object)
        board_object.movePiece(player2_next_move)
        print board_object.toString()
        

''' setBoard(board_object)'''

def createBoard():
    f = open('Board.txt')
    board_object = Board(f)
    return board_object

if __name__ == "__main__":
    main()

