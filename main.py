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

# game.black_player.pieces.append(King(2, 5))
# game.white_player.pieces.append(King(4, 3))

game.move("e2", "e4") #white
game.move("d7", "d5") #black
game.move("e4", "d5") #white
game.move("d8", "d5") #black
game.move("b1", "c3") #white
game.move("d5", "e5")  #black
game.move("c3", "b5")
# game.move("g1", "e2") #white

# print(game.white_player.checked)