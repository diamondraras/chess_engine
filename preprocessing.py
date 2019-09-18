from Game import *
from Position import *

with open("../dataset/500parties.txt", "r") as file:
    data = file.read()

eloLimit = 2800
lines = data.split('\n')[5:]
for i, line in enumerate(lines):
    vec = line.split(" ")
    
    if vec[2] == "1/2-1/2":
        # print(vec[0])
        lines[i] = ""
        break
    else :
        result = vec[2].split('-')
        try:
            # Always promote to Queen
            toBreak = False
            for e in vec:
                egalIndex = vec.index("=")
                if vec[egalIndex+1] !="Q":
                    lines[i]=""
                    toBreak = True
                    break
            if toBreak:
                break
                    
        except ValueError:
            pass
        whiteWinButWeak = not (int(result[0]) == 1 and int(vec[3]) > eloLimit)
        blackWinButWeak = not (int(result[1]) == 1 and int(vec[4]) > eloLimit)
        if whiteWinButWeak:
            lines[i] = ""
        elif blackWinButWeak:
            lines[i] = ""

sn = 0
bn = 0
hafa = 0
error = 0
# print(lines[1])

lines = [line for line in lines if line]
print(len(lines))
for i, line in enumerate(lines[2:3]):
    # print(line[2], line[3])
    game = Game()
    game.startGame()
    line = line.split(" ")
    games = [row.split(".")[1] for row in line[17:] if row]
    # print(games)

    pieces_notations = ["R", "B", "N", "Q", "K"]
    
    for j, move in enumerate(games):
        # print(move)
        if move[-1] == "+":
            move = move[:-1]

        try:
            egalIndex = move.index("=")
            move = move[:egalIndex]
        except Exception:
            pass


        if move == "O-O":
            sn = sn +1
            game.smallCastling()
            pass
        elif move == "O-O-O":
            bn = bn + 1
            game.bigCastling()
            # big castling
            pass
        else:
            precision = False
            try:
                _, dst = move.split("x")
                if len(_) == 1 and _ in pieces_notations:
                    type_of_piece = _
                elif len(_) == 1 and not (_ in pieces_notations):
                    type_of_piece = "P"
                    precision = _
                else:
                    type_of_piece = _[0]
                    precision = _[1]
            except Exception:
                if len(move) == 2:
                    dst = move
                    type_of_piece = "P"
                    # Pawn deplacement
                    pass
                elif len(move) == 3 and move[0] in pieces_notations:
                    type_of_piece = move[0]
                    dst = move[1:]
                    # Other piece deplacement
                elif len(move) != 3:
                    type_of_piece = move[0]
                    dst = move[-2:]
                    precision = move[1]
            if precision and type_of_piece != "P":
                hafa = hafa +1
                # print("move :", move, "\npiece :", type_of_piece, "\ndestination :", dst, "\nprecision :", precision, "\n\n")
            
            name = dict()
            name['N'] = "Knight"
            name['R'] = "Rook"
            name['K'] = "King"
            name['Q'] = "Queen"
            name['B'] = "Bishop"
            name['P'] = "Pawn"
            
            if len(game.moves) % 2 == 0:
                current_player = game.white_player
            else:
                current_player = game.black_player

            destination = toNumberCoord(dst)
            if not precision:
                for piece in current_player.pieces:
                    if piece.typeOf() == name[type_of_piece]:
                        piece_possibilities = piece.getPossiblesMoves(current_player)
                        if destination.isIn(piece_possibilities):
                            source = piece.positions
                            break
            else:
                # print(precision)
                sources = list()
                for piece in current_player.pieces:
                    if piece.typeOf() == name[type_of_piece]:
                        piece_possibilities = piece.getPossiblesMoves(current_player)
                        # print(piece_possibilities)
                        
                        if destination.isIn(piece_possibilities):
                            sources.append(piece.positions)
                            # print(piece.positions)
                # print(precision, sources)
                try:
                    y = int(precision)
                    for e in sources:
                        if e.y == y:
                            source = e
                            break

                except Exception:
                    
                    x = ord(precision) - 96
                    # print(x)
                    # print(x)
                    # print(sources)
                    for e in sources:
                        if e.x == x:
                            source = e
                            break

            # print(current_player.color,move)
            # game.move
            # game.moves.append(list())
            # print(source.convertAlgebrical(), destination.convertAlgebrical())
            # print(current_player.color, current_player.pieces, "\n\n")
            # print(current_player.color, current_player.opponent.pieces)
            game.move(source.convertAlgebrical(), destination.convertAlgebrical())
                # print(line)
                # error = error +1
                # print(j, move)
                # print(x)
                # print(precision)
                # raise Exception(e)
            # print(current_player.color, move)
            # print("source : ", source, "destination : ", destination, "type_of_piece : ", name[type_of_piece], end = "\n\n")
            
            # print(current_player.pieces)
            # print(destination)
            # print(source)
# print(error)
        # break
    # break
print("white :"+str(game.white_player.pieces))
print("black :"+str(game.black_player.pieces))
# print(sn, bn)
# print(hafa)