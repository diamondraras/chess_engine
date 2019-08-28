from Game import *
chess = Game()
chess.move("e2", "e4")
chess.move("d7", "d5")
chess.move("e4", "d5")
print(chess.black_player.pieces)