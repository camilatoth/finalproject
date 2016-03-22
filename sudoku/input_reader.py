from move import Move

class InputReader(object):

	def read_move(self):
		print "Place your move:row,column,number or quit"
		print "sudoku> ",

		raw_move = raw_input() # input (he reads what you type)

		if raw_move == "quit":
			return Move(0,0,0,True) # returns the instantiation of the class Move
		else:
			row_index, col_index, number = raw_move.split(',') # split function returns a list of strings
			return Move(int(row_index), int(col_index), int(number)) # returns the instantiation of the class Move with the variables above


		