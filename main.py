from Piece import *
from Piece.Pawn import *
from Piece.Rook import *
from Piece.Knight import *
from Piece.Bishop import *
from Piece.Queen import *
from Piece.King import *


from Game import *
game = Game()
# game.clearBoard()

# game.black_player.pieces.append(King(1, 1))
# game.black_player.pieces.append(Pawn(6, 1))
# # game.black_player.pieces.append(Knight(2, 6))
# game.white_player.pieces.append(King(1, 7))
# game.white_player.pieces.append(Queen(4, 3))

game.move("e2", "e4") #white
game.move("e7", "e5") #black
game.move("g1", "f3") #white
game.move("b8", "c6") #black
game.move("f1", "c4") #white
game.move("d8", "f6")  #black
game.smallCastling()
print(game.white_player.pieces)


# print(game.black_player.draws)