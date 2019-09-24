from Game import *
from Position import *
from ChessRulesExceptions import *
import os.path
import random
outputFile = "../dataset/chessgames.csv"

with open("../dataset/500parties.txt", "r") as file:
    data = file.read()
from csv import *
eloLimit = 2300
lines = data.split('\n')[5:]

toRemoveIndex = list()


for i, line in enumerate(lines):
    vec = line.split(" ")
    if vec[2] == "1/2-1/2":
        toRemoveIndex.append(i)
        continue
    else:
        result = vec[2].split('-')
        for e in vec:
            try:
                egalIndex = e.index("=")
                if e[egalIndex+1] !="Q":
                    toRemoveIndex.append(i)
                    break
            except Exception as error:
                break

        try:
            if result[0]:
                winner = "white"
                welolow = int(vec[3]) < eloLimit
                if welolow:
                    toRemoveIndex.append(i)
            else:
                winner = "black"
                belolow = int(vec[4]) < eloLimit
                if belolow:
                    toRemoveIndex.append(i)
            
        except ValueError as error:
            toRemoveIndex.append(i)



errorNumber = 0
print("Total of selected games :", len(lines) - len(toRemoveIndex))
datasetLen = 0


if os.path.exists(outputFile):
    print("removing existing file")
    os.remove(outputFile)

try:

    for i, element in enumerate(lines):
        # print("hello")
        splited = element.split(" ")
        game = Game()
        game.startGame()
        gameResult = splited[2].split('-')
        moves = [row.split(".")[1] for row in splited[17:] if row]
        
        oneGameDatas = list()
        if result[0]:
            winnerPlayer = game.white_player
        else:
            winnerPlayer = game.black_player
            
        hasError = False
        try:

            if not i in toRemoveIndex:
                pieces_notations = ["R", "B", "N", "Q", "K"]
                # print(len(moves))
                for j, move in enumerate(moves):

                    # Remove promotion notation
                    try:
                        egalIndex = move.index("=")
                        move = move[:egalIndex]
                    except Exception:
                        pass

                    try:
                        # Remove check notation
                        if move[-1] == "+":
                            move = move[:-1]
                        # Remove checkmate notation
                        if move[-1] == "#":
                            move = move[:-1]
                    except Exception:
                        pass

                    if len(game.moves) % 2 == 0:
                        current_player = game.white_player
                    else:
                        current_player = game.black_player


                    if move == "O-O":

                        try:


                            boardRepresentation = winnerPlayer.getBoard()

                            if current_player.color == "white":
                                sourceIndex = 4
                                destIndex = 6
                            else:
                                sourceIndex = 60
                                destIndex = 62
                            

                            sourceRepresentation = [0]*64
                            sourceRepresentation[sourceIndex] = 1
                            destinationRepresentation = [0]*64
                            destinationRepresentation[destIndex] = 1
                            data = boardRepresentation + sourceRepresentation + destinationRepresentation
                            oneGameDatas.append(data)



                            game.smallCastling()
                        except Exception as error:
                            print(splited[0], j)
                            print(current_player.color, move)
                            print("white", game.white_player.pieces)
                            print("black", game.black_player.pieces)
                            raise(error)
                        
                    elif move == "O-O-O":
                        try:
                            boardRepresentation = winnerPlayer.getBoard()

                            if current_player.color == "white":
                                sourceIndex = 4
                                destIndex = 2
                            else:
                                sourceIndex = 60
                                destIndex = 58
                            
                            sourceRepresentation = [0]*64
                            sourceRepresentation[sourceIndex] = 1
                            destinationRepresentation = [0]*64
                            destinationRepresentation[destIndex] = 1
                            data = boardRepresentation + sourceRepresentation + destinationRepresentation
                            oneGameDatas.append(data)

                            game.bigCastling()

                        except Exception as error:
                            print(splited[0], j)
                            print(current_player.color, move)
                            print("white", game.white_player.pieces)
                            print("black", game.black_player.pieces)
                            raise(error)

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
                        
                        name = dict()
                        name['N'] = "Knight"
                        name['R'] = "Rook"
                        name['K'] = "King"
                        name['Q'] = "Queen"
                        name['B'] = "Bishop"
                        name['P'] = "Pawn"
                        

                        destination = toNumberCoord(dst)
                        if not precision:
                            for piece in current_player.pieces:
                                if piece.typeOf() == name[type_of_piece]:
                                    piece_possibilities = piece.getPossiblesMoves(current_player)
                                    if destination.isIn(piece_possibilities) and current_player.acceptable(piece.positions, destination):
                                        source = piece.positions
                                        break
                        else:
                            sources = list()
                            for piece in current_player.pieces:
                                if piece.typeOf() == name[type_of_piece]:
                                    piece_possibilities = piece.getPossiblesMoves(current_player)
                                    if destination.isIn(piece_possibilities):
                                        sources.append(piece.positions)
                            # print("destination", destination)
                            # print("sources",sources)
                            try:
                                y = int(precision)
                                for e in sources:
                                    if e.y == y:
                                        source = e
                                        break

                            except Exception:
                                x = ord(precision) - 96
                                # print(x)
                                for e in sources:
                                    if e.x == x:
                                        source = e
                                        break
                        # print(source, destination)


                        # Save board and source/destination

                        boardRepresentation = winnerPlayer.getBoard()
                        sourceRepresentation = source.getRepresentation()
                        destinationRepresentation = destination.getRepresentation()
                        data = boardRepresentation + sourceRepresentation + destinationRepresentation
                        oneGameDatas.append(data)
                        try:
                            # print(current_player.checkmated)
                            # print(source.convertAlgebrical(), destination.convertAlgebrical())


                            game.move(source.convertAlgebrical(), destination.convertAlgebrical())
                        except PositionException as error:
                            errorNumber += 1
                            hasError = True
                            break
                        except CheckMateException as error:
                            errorNumber += 1
                            hasError = True
                            break
                        except CheckException as error:
                            errorNumber += 1
                            hasError = True
                            break
        except Exception :
            continue
            # break
        if not hasError:
            datasetLen += int(splited[5])
            with open(outputFile, "a", newline="") as csvfile:
                spamwriter = writer(csvfile, delimiter=";", quotechar='|')
                for _ in oneGameDatas:
                    # print(_)
                    spamwriter.writerow(_)
        # break

    print("total of error", errorNumber)
    print("total of datasets : ", datasetLen)
except KeyboardInterrupt:
    print("total of error", errorNumber)
    print("total of moves : ", datasetLen)

response = input("do you want to remove the duplicates and shuffle? (yes/no)")

if response == "yes":
    with open(outputFile, mode='r', encoding="utf-8") as csvfile:
        data = reader(csvfile, delimiter=";")
        filtered = list()
        i = 0
        for a in data:
            if a not in filtered:
                filtered.append(a)

    random.shuffle(filtered)
    print("total of filtered",len(filtered))
    os.remove(outputFile)
    with open(outputFile, "w", newline="") as csvfile:
        for e in filtered:
            spamwriter = writer(csvfile, delimiter=";", quotechar='|')
            spamwriter.writerow(e)