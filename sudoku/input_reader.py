from move import Move

class InputReader(object):

	def read_move(self):
		print "Place your move:row,column,number or quit"
		print "sudoku> ",

		raw_move = raw_input()

		if raw_move == "quit":
			return Move(0,0,0,True)
		else:
			row_index, col_index, number = raw_move.split(',')
			return Move(int(row_index), int(col_index), int(number))


		