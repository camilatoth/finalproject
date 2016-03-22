from puzzles import PuzzlesGenerator

class Board(object):
	def __init__(self):
		self.game_board = PuzzlesGenerator().random_puzzle()

	def print_board(self):
		print " "  , 

		for i in range(9): # prints the index of the board
			print "%i" % (i) , 
	
		print ""

		for row_index in range(9):	
			print  row_index  , 
			for col_index in range(9):
				if self.game_board[row_index][col_index] == 0:
					print "_"	,
				else:
					print self.game_board[row_index][col_index] , 

			print ""

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
		for row_index in range(9):
			for col_index in range(9):
				if self.game_board[row_index][col_index] == 0:
					return False
		return True		

	def three_grid_range(self, index):
		if index in [0, 1, 2]:
			return range(0,3)
		elif index in [3, 4, 5]:
			return range(3,6)
		else:
			return range(6,9)

	def has_number_in_three_grid(self, row_index, col_index, number):
		row_range = self.three_grid_range(row_index) 				
		col_range = self.three_grid_range(col_index) 

		for row_index in row_range:
			for col_index in col_range:
				if self.game_board[row_index][col_index] == number:
					return True
		return False 










