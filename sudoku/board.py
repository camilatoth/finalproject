class Board(object):
	def __init__(self):
		self.game_board = [[0] * 9 for i in range(9)]


	def print_board(self):
		for line in self.game_board:
			print line

	def is_position_available(self, row_index, col_index):
		if self.game_board[row_index][col_index] == 0:
			return True
		else:
			return False

   	def is_number_valid(self, number):
		if  1 <= number <= 9: 
			return True
		else:
			return False

	def row_has_number(self, row_index, number):
		for x in self.game_board[row_index]:
			if x == number:
				return True
		return False
    
	def column_has_number(self, col_index, number):
		for row_index in range(9):
			if self.game_board[row_index][col_index] == number:
				return True
		return False

	def place_number(self, row_index, col_index, number):
		self.game_board[row_index][col_index] = number

	def is_game_over(self):
		for row_index in range(1,10):
			for col_index in range(1,10):
				if self.game_board[row_index][col_index] == 0:
					return False
		return True		 










