class Move(object):
	def __init__(self, row_index, col_index, number, quit = False):
		self.row_index = row_index
		self.col_index = col_index
		self.number = number
		self.quit = quit


	def is_quit(self):
		return self.quit
		