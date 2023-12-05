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
        #get the best move available; ignore the best score returned from minimax function
        _, best_move = self.minimax(board, self.depth, self.symbol)
        return best_move

    def minimax(self, board, depth, turn):
        legalMoves = game_rules.getLegalMoves(board, turn) #use only legal moves

        #check if there are more moves to be made
        if depth == 0 or not legalMoves:
            #evaluate board configuration for player
            return self.h1(board), None

        #initialize best move; no best move chosen at start
        best_move = None

        #if it's currently the opponent's turn
        if self.symbol != turn:
            
            #start at best score for opponent and find worse for them
            best_score = POS_INF

            #evaluates each position/child of position
            for move in legalMoves:

                #create new board state for each simulated move and evaluate possible score
                new_board = game_rules.makeMove(board, move)
                result = self.minimax(new_board, depth - 1, 'o' if turn == 'x' else 'x')
                score = result[0]  # get the score from the result tuple

                #update best possible score and move (minimize score for opponent)
                if score < best_score:
                    best_score = score
                    best_move = move

            return best_score, best_move
        
        #if it's your turn
        else:

            #start at worst score and try to find one that's better
            best_score = NEG_INF

            #evaluates each position/child of position
            for move in legalMoves:

                #create new board state for each simulated move and evaluate possible score
                new_board = game_rules.makeMove(board, move)
                result = self.minimax(new_board, depth - 1, 'o' if turn == 'x' else 'x')
                score = result[0]  # get the score from the result tuple

                #update if current score is better than best_score (maximize score for you)
                if score > best_score:
                    best_score = score
                    best_move = move

            return best_score, best_move


# This class has been replaced with the code for a deterministic player.
class AlphaBetaPlayer(Player):
    def __init__(self, symbol, depth): 
        super(AlphaBetaPlayer, self).__init__(symbol)
        self.depth = depth
        self.memo = {}

    # Leave these two functions alone.
    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    # Edit this one here. :)
    def getMove(self, board):
         #get the best move available; ignore the best score returned from alpha_beta function
        _, best_move = self.alpha_beta(board, self.depth, self.symbol, NEG_INF, POS_INF)
        return best_move

    def alpha_beta(self, board, depth, turn, alpha, beta):
        #convert the board to a hashable type for memoization to avoid timeout
        board_key = tuple(tuple(row) for row in board)

        #check if we have already computed the value for this board and depth
        if (board_key, depth, turn) in self.memo:
            #create self.memo dict to store results of previous calculations --> reduces number calculations needed and avoids repetition
            return self.memo[(board_key, depth, turn)]

        #use only legal moves
        legalMoves = game_rules.getLegalMoves(board, turn)
        if depth == 0 or not legalMoves:
            score = self.h1(board)

            #store score and corresponding board state in self.memo
            self.memo[(board_key, depth, turn)] = (score, None)
            return score, None

        best_move = None

        #for the opponent
        if self.symbol != turn:
            #initalize to find min score
            best_score = POS_INF
            for move in legalMoves:
                new_board = game_rules.makeMove(board, move)
                result = self.alpha_beta(new_board, depth - 1, 'o' if turn == 'x' else 'x', alpha, beta)
                score = result[0]
                if score < best_score:
                    best_score = score
                    best_move = move

                #update beta value where beta = best score maximizing player is assured of
                beta = min(beta, best_score)

                #prune
                if beta <= alpha:
                    break

            #update self.memo
            self.memo[(board_key, depth, turn)] = (best_score, best_move)
            
            return best_score, best_move
        
        #for the current player/you
        else:
            #initialize to find max score
            best_score = NEG_INF 
            for move in legalMoves:
                new_board = game_rules.makeMove(board, move)
                result = self.alpha_beta(new_board, depth - 1, 'o' if turn == 'x' else 'x', alpha, beta)
                score = result[0]
                if score > best_score:
                    best_score = score
                    best_move = move
                
                #update alpha value where alpha = best score minimizing player assured of
                alpha = max(alpha, best_score)

                #prune
                if alpha >= beta:
                    break
            
            #update self.memo
            self.memo[(board_key, depth, turn)] = (best_score, best_move)
            
            return best_score, best_move


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