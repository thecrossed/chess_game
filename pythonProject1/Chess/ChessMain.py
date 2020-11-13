"""
This is our main driver file. It will be responsible for handling user input and displaying the current GameState object.
"""

import pygame as p 
from Chess import ChessEngine

WIDTH = HEIGHT = 512 # 400 is another option
DIMENSION = 8 # dimensions of a chess board is 8 * 8
SQ_SIZE = HEIGHT // DIMENSION 
MAX_FPS = 15 # for animations later on
IMAGES = {}

"""
Initiaize a global dictionary of images. This will be called exacty once in the main
"""

def loadImages():
	pieces = ["wp", "wR", "wB", "wN", "wQ", "wK", "bp", "bR", "bB", "bN", "bQ", "bK"]
	for piece in pieces:
		IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png") , (SQ_SIZE, SQ_SIZE))
	# Note: We can access an image by saying 'IMAGES['wp']'

'''
The main driver fo our code. This will hadlne user input and updating the graphics
'''
def main():
	p.init()
	screen = p.display.set_mode((WIDTH, HEIGHT))
	clock = p.time.Clock()
	screen.fill(p.Color("white"))
	gs = ChessEngine.GameState()
	print(gs.board)

main()