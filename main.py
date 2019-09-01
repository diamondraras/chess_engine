from Piece import *
from Piece.Pawn import *
from Piece.Rook import *
from Piece.Knight import *
from Piece.Bishop import *
from Piece.Queen import *
from Piece.King import *


from Game import *
game = Game()
game.clearBoard()

game.black_player.pieces.append(King(2, 1))
game.white_player.pieces.append(King(2, 3))
game.white_player.pieces.append(Queen(4, 2))

game.move("b3", "c2") #white
game.move("b1", "a1")  #white
game.move("d2", "a5")
# game.move("b1", "a1") #white
# game.move("d1", "e1") #black
print(game.black_player.checkmated)
# print(game.white_player.checked)