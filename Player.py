from Piece import *
from Piece.Pawn import *
from Piece.Rook import *
from Piece.Knight import *
from Piece.Bishop import *
from Piece.Queen import *
from Piece.King import *
from ChessRulesExceptions import PositionException
from ChessRulesExceptions import CheckException
from ChessRulesExceptions import CheckMateException
from ChessRulesExceptions import CastingException
from Position import *
from copy import *
class Player(object):
    def __init__(self, color):
        self.color = color
        self.new_game()
        self.checked = False
        self.checkmated = False
        self.draws = False
    
    def movePiece(self, sourcePosition, destinationPosition, game):

        # Le jeu ne peut pas continuer si le joueur courant est en echec et mat
        if self.checkmated:
            raise CheckMateException(self.color + " is already checkmated !")
        
        # Trouver la pièce en cours de déplacement
        piece = self.findPiece(sourcePosition)
        if not self.checked:
            
            # Mouvement normal si le joueur n'est pas en échec 
            piece.changePosition(destinationPosition, self, game)
        else:

            # Checher tous les coups permettant d'éviter l'échec
            acceptableAvoidingCheck = self.acceptable(sourcePosition, destinationPosition)
            
            # Le joueur doit éviter l'échec s'il est attaqué par son adversaire sinon erreur
            if self.checked and acceptableAvoidingCheck:
                piece.changePosition(destinationPosition, self, game)
                self.checked = False
            else:
                raise CheckException("Check positions must be prevented !")
            
    def acceptable(self, sourcePosition, destinationPosition):

        # On clone l'objet pour éviter les mutations à l'objet original mais ça pas vraiment fonctionné ... :p
        tempPlayer = copy(self)

        # On cherche tous les pieces du joueur en cours 
        all_pieces = tempPlayer.pieces

        # Quel est la piece qui sera deplacée
        piece_to_move = tempPlayer.findPiece(sourcePosition)

        # L'indice dans le tableau regroupant tous les pièces
        index_of_piece = all_pieces.index(piece_to_move)

        # On essaye de changer la pièces à la position demandé
        piece_to_move.positions = destinationPosition

        # On mute l'objet original pour la nouvelle piece avec la nouvelle position
        tempPlayer.pieces[index_of_piece] = piece_to_move

        # On vérifie si le joueur est toujours en échecs
        tempPlayer.check()

        # On retoure la position muté à sa position originale
        piece_to_move.positions = sourcePosition
        tempPlayer.pieces[index_of_piece] = piece_to_move
        
        # Si ce coup est acceptabe pour éviter l'echec
        return tempPlayer.checked == False

    def getKing(self):
        for piece in self.pieces:
            if piece.typeOf() == "King":
                return piece

    def findPiece(self,positions):
        for piece in self.pieces:
            if piece.positions.equals(positions):
                return piece
        raise PositionException(self.color+" : No matching piece in x="+str(positions.x)+",y="+str(positions.y))

    def hasPiece(self, positions):
        for piece in self.pieces:
            if piece.positions.equals(positions):
                return True
        return False

    def new_game(self):
        pieces = list()

        # Pawn initialisation
        for i in range(1,9):
            if self.color == "black":
                pieces.append(Pawn(i, 7))
            if self.color == "white":
                pieces.append(Pawn(i, 2))
                
        # Rook initialisation
        if self.color == "black":
            pieces.append(Rook(1, 8))
            pieces.append(Rook(8, 8))
        if self.color == "white":
            pieces.append(Rook(1, 1))
            pieces.append(Rook(8, 1))
            
        # Knight initialisation
        if self.color == "black":
            pieces.append(Knight(2, 8))
            pieces.append(Knight(7, 8))
        if self.color == "white":
            pieces.append(Knight(2, 1))
            pieces.append(Knight(7, 1))
        
        # Bishop initialisation
        if self.color == "black":
            pieces.append(Bishop(3, 8))
            pieces.append(Bishop(6, 8))
        if self.color == "white":
            pieces.append(Bishop(3, 1))
            pieces.append(Bishop(6, 1))

        # Queen initialisation
        if self.color == "black":
            pieces.append(Queen(4, 8))
        if self.color == "white":
            pieces.append(Queen(4, 1))

        # King initialisation
        if self.color == "black":
            pieces.append(King(5, 8))
        if self.color == "white":
            pieces.append(King(5, 1))

        self.pieces = pieces

    def remove_passable(self):
        for piece in self.pieces:
            if piece.typeOf() == "Pawn":
                piece.passable = False

    def remove_piece(self, positions):
       for i, piece in enumerate(self.pieces):
            if piece.positions.equals(positions):
                del self.pieces[i]

    def checkmate(self):

        # L'état initial n'est pas en échec et mat
        self.checkmated = False
        king = self.getKing()
        king_dangerous_positions = king.getDangerousPositions(self)
        king_in_danger = king.positions.isIn(king_dangerous_positions)

        # Seulement si le roi est en danger
        if king_in_danger:
            self.checked = True
            # On suppose qu'il est en échec et mat
            mateable = True

            # On recherche tous les coups possibles de toutes les pièces
            for piece in self.pieces:
                for move in piece.getPossiblesMoves(self):

                    # Si un seul coup permet de mettre le roi à l'abri alors pas d'échec et mat
                    if self.acceptable(piece.positions, move):
                        mateable = False
                        break
                if not mateable:
                    print(piece,move)
                    break
            
            print(mateable)
            # Si cette variable reste True alors le joueur a perdu ..
            if mateable:
                self.checkmated = True

    def check(self):
        self.checked = False
        king = self.getKing()

        # On recherche tous les positions que le roi ne poura pas aller
        king_dangerous_positions = king.getDangerousPositions(self)

        # Si le roi est dans une position dangeureuse
        king_in_danger = king.positions.isIn(king_dangerous_positions)
        if king_in_danger:
            self.checked = True

    def drawsCheck(self):
        self.draws = False
        king = self.getKing()
        king_dangerous_positions = king.getDangerousPositions(self)
        king_in_danger = king.positions.isIn(king_dangerous_positions)

        possibles_moves = list()

        # Si le roi n'est pas en danger et le joueur n'est pas en echec et mat
        if not king_in_danger and not self.checkmated:

            # On cherche tous les coups de toutes les pièces
            for piece in self.pieces:
                possibles_moves += piece.getPossiblesMoves(self)

            # Si aucun mouvement est possible alors il y a egalité
            if len(possibles_moves) == 0:
                self.draws = True
                self.opponent.draws = True
            else :
                self.draws = False
                self.opponent.draws = False
    
    def getPieceIndex(self, positions):
        for i, piece in enumerate(self.pieces):
            if piece.positions.equals(positions):
                return i
        raise PositionException("No pieces found in " + positions)
    

    def smallCastling(self):

        # La position des pièces dépend de la couleur des joueurs
        if self.color == "white":
            knight_position = Position(7, 1)
            bishop_position = Position(6, 1)
            rook_position = Position(8, 1)
        elif self.color == "black":
            knight_position = Position(7, 8)
            bishop_position = Position(6, 8)
            rook_position = Position(8, 8)

        possibles_opponent_moves = list()

        # Recherche de tous les coups de l'adversaire
        for piece in self.opponent.pieces:
            possibles_opponent_moves = possibles_opponent_moves + piece.getPossiblesMoves(self.opponent)


        rook = self.findPiece(rook_position)
        king = self.getKing()
        bishop_not_here = not self.hasPiece(bishop_position)
        knight_not_here = not self.hasPiece(knight_position)
        movement = not rook.moved and not king.moved
        smallCastlingPossible = movement \
                                and bishop_not_here \
                                and knight_not_here \
                                and not bishop_position.isIn(possibles_opponent_moves) \
                                and not knight_position.isIn(possibles_opponent_moves)
        # Si tous les conditions de roque sont satisfaites
        if smallCastlingPossible:
            if self.color == "white":
                self.pieces[self.getPieceIndex(rook_position)].positions = Position(6, 1)
                self.pieces[self.getPieceIndex(king.positions)].positions = Position(7, 1)
            elif self.color == "black":
                self.pieces[self.getPieceIndex(rook_position)].positions = Position(6, 8)
                self.pieces[self.getPieceIndex(king.positions)].positions = Position(7, 8)
        else:
            raise CastingException("small castling impossible")

    def bigCastling(self):
        if self.color == "white":
            knight_position = Position(2, 1)
            bishop_position = Position(3, 1)
            rook_position = Position(1, 1)
            queen_position = Position(4, 1)
        elif self.color == "black":
            knight_position = Position(7, 8)
            bishop_position = Position(6, 8)
            rook_position = Position(8, 8)
            queen_position = Position(4, 8)

        possibles_opponent_moves = list()

        for piece in self.opponent.pieces:
            possibles_opponent_moves = possibles_opponent_moves + piece.getPossiblesMoves(self.opponent)
        rook = self.findPiece(rook_position)
        king = self.getKing()
        bishop_not_here = not self.hasPiece(bishop_position)
        knight_not_here = not self.hasPiece(knight_position)
        queen_not_here = not self.hasPiece(queen_position)
        movement = not rook.moved and not king.moved
        big_castling_possible = movement \
                                and bishop_not_here \
                                and knight_not_here \
                                and queen_not_here \
                                and not bishop_position.isIn(possibles_opponent_moves) \
                                and not knight_position.isIn(possibles_opponent_moves) \
                                and not queen_position.isIn(possibles_opponent_moves)
        if big_castling_possible:
            if self.color == "white":
                self.pieces[self.getPieceIndex(rook_position)].positions = Position(4, 1)
                self.pieces[self.getPieceIndex(king.positions)].positions = Position(3, 1)
            elif self.color == "black":
                self.pieces[self.getPieceIndex(rook_position)].positions = Position(4, 8)
                self.pieces[self.getPieceIndex(king.positions)].positions = Position(3, 8)
        else:
            raise CastingException("big castling impossible")