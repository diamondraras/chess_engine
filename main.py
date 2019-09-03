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

# game.white_player.pieces.append(King(1, 2))
# game.black_player.pieces.append(King(1, 7))
# game.white_player.pieces.append(Pawn(1, 7))
# game.move("a7", "a8")
# print(game.white_player.pieces)

while True:
    try:
        move = input(game.turnOf()+" "+str(int(len(game.moves)/2)+1)+" : ")
    except TypeError:
        pass
    except KeyboardInterrupt:
        break
    
    if move =="O-O":
        game.smallCastling()
    elif move =="O-O-O":
        game.bigCastling()
    else:
        src, dest = move.split(" ")
        try:
            game.move(src, dest)
        except Exception:
            pass
        if game.white_player.checked:
            print("Les blancs sont en échecs")
        elif game.black_player.checked:
            print("Les noirs sont en échecs")
        if game.black_player.checkmated and game.black_player.checked:
            print("Les noirs sont en échecs et mat")
            break
        if game.white_player.checkmated  and game.black_player.checked:
            print("Les blancs sont en échecs et mat")
        if game.white_player.draws and game.black_player.draws:
            print("Egalité")
            break
print("white : " + str(game.white_player.pieces))
print("black : " + str(game.black_player.pieces))
# print(game.black_player.draws)