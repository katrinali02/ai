import game_rules, random
###########################################################################
# Explanation of the types:
# The board is represented by a row-major 2D list of characters, 0 indexed
# A point is a tuple of (int, int) representing (row, column)
# A move is a tuple of (point, point) representing (origin, destination)
# A jump is a move of length 2
###########################################################################

# I will treat these like constants even though they aren't
# Also, these values obviously are not real infinity, but close enough for this purpose
NEG_INF = -1000000000
POS_INF = 1000000000

class Player(object):
    """ This is the player interface that is consumed by the GameManager. """
    def __init__(self, symbol): self.symbol = symbol # 'x' or 'o'

    def __str__(self): return str(type(self))

    def selectInitialX(self, board): return (0, 0)
    def selectInitialO(self, board): pass

    def getMove(self, board): pass

    def h1(self, board):
        return -len(game_rules.getLegalMoves(board, 'o' if self.symbol == 'x' else 'x'))


# This class has been replaced with the code for a deterministic player.
class MinimaxPlayer(Player):
    def __init__(self, symbol, depth): 
        super(MinimaxPlayer, self).__init__(symbol)
        self.depth = depth

    # Leave these two functions alone.
    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    # Edit this one here. :)
    def getMove(self, board):
        _, best_move = self.minimax(board, self.depth, self.symbol)
        return best_move

    def minimax(self, board, depth, turn):
        legalMoves = game_rules.getLegalMoves(board, turn)
        if depth == 0 or not legalMoves:
            return self.h1(board), None

        best_move = None
        if self.symbol != turn:
            best_score = POS_INF
            for move in legalMoves:
                new_board = game_rules.makeMove(board, move)
                result = self.minimax(new_board, depth - 1, 'o' if turn == 'x' else 'x')
                score = result[0]  # Get the score from the result tuple
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move
        else:
            best_score = NEG_INF
            for move in legalMoves:
                new_board = game_rules.makeMove(board, move)
                result = self.minimax(new_board, depth - 1, 'o' if turn == 'x' else 'x')
                score = result[0]  # Get the score from the result tuple
                if score > best_score:
                    best_score = score
                    best_move = move

            return best_score, best_move


# This class has been replaced with the code for a deterministic player.
class AlphaBetaPlayer(Player):
    def __init__(self, symbol, depth): 
        super(AlphaBetaPlayer, self).__init__(symbol)
        self.depth = depth

    # Leave these two functions alone.
    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    # Edit this one here. :)
    def getMove(self, board):
        alpha = NEG_INF
        beta = POS_INF

        best_move, score = self.alpha_beta(board, self.depth, alpha, beta, self.symbol)
        return best_move
        # legalMoves = game_rules.getLegalMoves(board, self.symbol)
        # if not legalMoves:
        #     return None

        # best_move = None
        

        # for move in legalMoves:
        #     new_board = game_rules.makeMove(board, move)
        #     score = self.alpha_beta(new_board, self.depth - 1, alpha, beta, "o" if self.symbol == 'x' else "x")
        #     if (self.symbol == 'x' and score > alpha) or (self.symbol == 'o' and score < beta):
        #         if self.symbol == 'x':
        #             alpha = score
        #         else:
        #             beta = score
        #         best_move = move

        # return best_move

    def alpha_beta(self, board, depth, alpha, beta, turn):
        if self.symbol != turn:

            legalMoves = game_rules.getLegalMoves(board, turn)
            if depth == 0 or  len(legalMoves) < 1:
                return None, self.h1(board)
            
            opt = NEG_INF
            for move in legalMoves:
                new_board = game_rules.makeMove(board, move)
                m,score = self.alpha_beta(new_board, depth - 1, alpha, beta, 'o' if turn == 'x' else 'x')
                
                if opt < score:
                    best_move, opt = move,score

                if opt >= beta:
                    return best_move

                if opt > alpha:
                    alpha = opt    
                
            return best_move,opt
        else:
            legalMoves = game_rules.getLegalMoves(board, turn)
            if depth == 0 or  len(legalMoves) < 1:
                return None, self.h1(board)
            opt = POS_INF
            for move in legalMoves:
                new_board = game_rules.makeMove(board, move)
                m, score = self.alpha_beta(new_board, depth - 1, alpha, beta, 'o' if turn == 'x' else 'x')

                if opt > score:
                    best_move, opt = move,score

                if opt <= alpha:
                    return best_move,opt

                if opt < beta:
                    beta = opt  
            return best_move,opt


class RandomPlayer(Player):
    def __init__(self, symbol):
        super(RandomPlayer, self).__init__(symbol)

    def selectInitialX(self, board):
        validMoves = game_rules.getFirstMovesForX(board)
        return random.choice(list(validMoves))

    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return random.choice(list(validMoves))

    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0: return random.choice(legalMoves)
        else: return None


class DeterministicPlayer(Player):
    def __init__(self, symbol): super(DeterministicPlayer, self).__init__(symbol)

    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0: return legalMoves[0]
        else: return None


class HumanPlayer(Player):
    def __init__(self, symbol): super(HumanPlayer, self).__init__(symbol)
    def selectInitialX(self, board): raise NotImplementedError('HumanPlayer functionality is handled externally.')
    def selectInitialO(self, board): raise NotImplementedError('HumanPlayer functionality is handled externally.')
    def getMove(self, board): raise NotImplementedError('HumanPlayer functionality is handled externally.')


def makePlayer(playerType, symbol, depth=1):
    player = playerType[0].lower()
    if player   == 'h': return HumanPlayer(symbol)
    elif player == 'r': return RandomPlayer(symbol)
    elif player == 'm': return MinimaxPlayer(symbol, depth)
    elif player == 'a': return AlphaBetaPlayer(symbol, depth)
    elif player == 'd': return DeterministicPlayer(symbol)
    else: raise NotImplementedError('Unrecognized player type {}'.format(playerType))

def callMoveFunction(player, board):
    if game_rules.isInitialMove(board): return player.selectInitialX(board) if player.symbol == 'x' else player.selectInitialO(board)
    else: return player.getMove(board)