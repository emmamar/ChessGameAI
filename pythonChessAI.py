from Board import Board
from Player import Player

def main():
    board_object = createBoard()
    player1_computer = Player(white)
    player2_computer = Player(black)
    while not board_object.is_check_mate():
        player1_next_move = player1_computer.determineNextMove(board_object)
        board_object.changeBoard(board_object, player1_next_move)
        if not board_object.is_check_mate():
            player2_next_move = player2_computer.determineNextMove(board_object)
            board_object = changeBoard(board_object, player2_next_move)

        

''' setBoard(board_object)'''

def createBoard():
    f = open('Board.txt')
    board_object = Board(f)
    return board_object

def determineNextMove(board_object, player):
    '''if player = white:'''
    	board_object.get_available_white_moves()
    '''else:'''
        board_object.get_available_black_moves()
    '''get available moves, choose from them'''
    '''set the best move into the board obj and return'''
    return board_object

'''def setBoard(board_object):
f = open('Board.txt', 'w')
f.write(board_object.toString())
'''

if __name__ == "__main__":
    main()

