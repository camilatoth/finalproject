from board import Board
from input_reader import InputReader
from judge import Judge

class Sudoku(object):
	def __init__(self):
		self.board = Board()
		self.input_reader = InputReader()
		self.judge = Judge(self.board)


	def start_game(self):
		print "Welcome to Sudoku!"

		while not self.board.is_game_over():
			self.board.print_board()
			move = self.input_reader.read_move()
			
			if move.is_quit():
				quit()

			if self.judge.is_valid_move(move.row_index, move.col_index, move.number):
				self.board.place_number(move.row_index, move.col_index, move.number)

			else:
				print "That is not a valid movement. Try again!"


sudoku = Sudoku()
sudoku.start_game()
