
class Piece():

  def __init__(self, c, px, py):
    pass
  
  def get_available_moves(self, board):
    test_set = self.available_moves
    available = list()

    for move in test_set:
      if self.not_check(board, move):
        available += move
    return available

  def not_check(self, board, move_to_try):
    can_move = board.try_move_piece(
      move_to_try
    )
    no_check = can_move and not board.is_check(self.color)
    board.undo()
    return no_check
  
  