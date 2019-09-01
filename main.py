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

game.black_player.pieces.append(King(1, 1))
game.black_player.pieces.append(Pawn(6, 1))
# game.black_player.pieces.append(Knight(2, 6))
game.white_player.pieces.append(King(1, 7))
game.white_player.pieces.append(Queen(4, 3))

game.move("d3", "c2")

print(game.black_player.draws)