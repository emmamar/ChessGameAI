from Board import Board

def main():
    board_object = createBoard()
    board_object = determineNextMove(board_object)

''' setBoard(board_object)'''

def createBoard():
    f = open('Board.txt')
    board_object = Board(f)
    return board_object

def determineNextMove(board_object):
    board_object.get_available_white_moves()

    '''get available moves, choose from them'''
    '''set the best move into the board obj and return'''
    return board_object

'''def setBoard(board_object):
f = open('Board.txt', 'w')
f.write(board_object.toString())
'''

if __name__ == "__main__":
    main()

