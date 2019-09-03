from Game import *
from Position import *

with open("../dataset/500parties.txt", "r") as file:
    data = file.read()

eloLimit = 2800
lines = data.split('\n')[5:]
for i, line in enumerate(lines):
    vec = line.split(" ")
    
    if vec[2] == "1/2-1/2":
        print(vec[0])
        del lines[i]
    else :
        result = vec[2].split('-')
        try:
            # Always promote to Queen
            for e in vec:
                egalIndex = vec.index("=")
                if vec[egalIndex+1] !="Q":
                    del lines[i]
            
        except ValueError:
            pass
        try:
            whiteWinButWeak = not (int(result[0]) == 1 and int(vec[3]) > eloLimit)
            blackWinButWeak = not (int(result[1]) == 1 and int(vec[4]) > eloLimit)
            if whiteWinButWeak:
                del lines[i]
            elif blackWinButWeak:
                del lines[i]
            
        except Exception:
            del lines[i]

sn = 0
bn = 0
hafa = 0
# print(len(lines))
for i, line in enumerate(lines):
    game = Game()
    game.startGame()
    line = line.split(" ")
    games = [row.split(".")[1] for row in line[17:] if row]
    print(games)

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
            try:
                game.move(source.convertAlgebrical(), destination.convertAlgebrical())
            except Exception as e:
                print(line)
                # print(j, move)
                # print(x)
                # print(precision)
                raise Exception(e)
            # print(current_player.color, move)
            # print("source : ", source, "destination : ", destination, "type_of_piece : ", name[type_of_piece], end = "\n\n")
            
            # print(current_player.pieces)
            # print(destination)
            # print(source)
                
        # break
    # break
# print(sn, bn)
# print(hafa)