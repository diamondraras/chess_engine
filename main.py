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

game.white_player.pieces.append(King(2, 3))
game.black_player.pieces.append(King(2, 5))

print(game.black_player.pieces)
print(game.white_player.pieces)

game.move("b3", "b4")