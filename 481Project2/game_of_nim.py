from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[3,1]):
        # Initialize GameState.
        moves = []
        for x in range(0, len(board)):
            for y in range(0, board[x]):
                moves.append((x, y+1))
        self.initial = GameState(to_move='X', utility=0, board=board, moves=moves)

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def result(self, state, move):
        # Copy board and update it with move.
        board = state.board.copy()
        x = move[0]
        y = move[1]
        board[x] = board[x] - y

        # Copy the moves list.
        moves = list(state.moves)
        NewMoves = moves.copy()

        # Remove all instances where move[0] == x from NewMoves.
        for move in moves:
            if move[0] == x:
                NewMoves.remove(move)
        # Add new moves to NewMoves to account for modification of the list of moves.
        for y in range(0, board[x]):
            NewMoves.append((x, y+1))
        
        # Return a new instance of GameState.
        return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                         utility=self.utility(state, state.to_move),
                         board=board, moves=NewMoves)

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        player = state.to_move
        # If player is 'X', return +1.
        if player == 'X':
            if len(state.moves) == 0:
                return +1
        # If player is 'O', return -1.
        if player == 'O':
            if len(state.moves) == 0:
                return -1
        return 0

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return len(state.moves) == 0

    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3) ))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")