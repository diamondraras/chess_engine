from Game import *
chess = Game()
chess.move("e2", "e4")
chess.move("d7", "d5")
chess.move("e4", "d5")
chess.move("g8", "f6")
chess.move("b1", "c3")
chess.move("f6", "d5")

print(chess.white_player.pieces)