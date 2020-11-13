"""
This class is responsible for storing all the information about the current stats of a chess game. It will also be responbile
for determing the valid moves at the current state. It will also keep a move lag.
"""

class GameState():
	def __init__(self):
		# board is an 8*8 2d list, each element of the list has 2 characters.
		# the first character represents the color of piece, b or w
		# the second character represesnts the type of the piece
		# "--" represents an empty space with no piece
		self.board = [
			["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
			["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
			["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

 