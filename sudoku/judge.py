from board import Board

class Judge(object):
	def __init__(self, board):
		self.board = board
	
	def is_valid_move(self, row_index, col_index, number):
		position_available = self.board.is_position_available(row_index, col_index)
		number_valid = self.board.is_number_valid(number)
		number_in_row = self.board.row_has_number(row_index, number)
		number_in_column = self.board.column_has_number(col_index, number)
		number_in_three_grid = self.board.has_number_in_three_grid(row_index, col_index, number)

		return (position_available and number_valid and (not number_in_row) and (not number_in_column) and (not number_in_three_grid))





