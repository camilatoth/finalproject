game_board = [[0] * 9 for i in range(9)]

def three_grid_range(index):
	if index in [0, 1, 2]:
		return range(0,3)
	elif index in [3, 4, 5]:
		return range(3,6)
	else:
		return range(6,9)

def has_number_in_three_grid(board, row_index, col_index, number):
	row_range = three_grid_range(row_index) 				
	col_range = three_grid_range(col_index) 

	for row_index in row_range:
		for col_index in col_range:
			if board[row_index][col_index] == number:
				return True
	return False			

print three_grid_range(4)




def three_grid_range(self, index):
	if index in [0, 1, 2]:
		return range(0,3)
	elif index in [3, 4, 5]:
		return range(3,6)
	else:
		return range(6,9)

def has_number_in_three_grid(self, row_index, col_index, number):
	row_range = three_grid_range(row_index) 				
	col_range = three_grid_range(col_index) 

	for row_index in row_range:
		for col_index in col_range:
			if self.game_board[row_index][col_index] == number:
				return True
	return False







