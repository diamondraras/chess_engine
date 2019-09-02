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

game.white_player.pieces.append(King(1, 2))
game.black_player.pieces.append(King(1, 7))
game.white_player.pieces.append(Pawn(1, 7))
game.move("a7", "a8")
print(game.white_player.pieces)


# print(game.black_player.draws)