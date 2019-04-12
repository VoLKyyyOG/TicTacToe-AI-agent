"""
Minimax algorithm.
State - Current state of board.
Depth - Current depth of game tree.
Player - AGENT or HUMAN.

Also includes the list of functions required for the main.py

FILENAME: agent.py
"""

# Import libraries
from math import inf

# Global Variables
BOARD = [
    [0, 0 ,0],
    [0, 0, 0],
    [0, 0, 0]
]

ACTIONS = {
    1: [0, 0], 2: [0, 1], 3: [0, 2],
    4: [1, 0], 5: [1, 1], 6: [1, 2],
    7: [2, 0], 8: [2, 1], 9: [2, 2],
}

HUMAN = -1
AGENT = +1
NONE = 0

BLANK = ' '
LINE = '\n---------------'

# Functions
def eval(state):
    """
    Evaluation function.
    Returns: +1 if Agent wins, -1 if Human wins, 0 for draw.
    """
    if winner(state, AGENT):
        return +1
    elif winner(state, HUMAN):
        return -1
    else:
        return 0

def winner(state, player):
    """
    Function to checks if a player has a winning combination.
    Returns: True if the player specified has won.
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]], # Row 1
        [state[1][0], state[1][1], state[1][2]], # Row 2
        [state[2][0], state[2][1], state[2][2]], # Row 3
        [state[0][0], state[1][0], state[2][0]], # Col 1
        [state[0][1], state[1][1], state[2][1]], # Col 2
        [state[0][2], state[1][2], state[2][2]], # Col 3
        [state[0][0], state[1][1], state[2][2]], # Diag 1
        [state[2][0], state[1][1], state[0][2]], # Diag 2
    ]
    return True if [player, player, player] in win_state else False

def game_over(state):
    """
    Function to test if one of the players has won.
    Returns: True if Agent or Human wins.
    """
    return winner(state, AGENT) or winner(state, HUMAN)

def blank_tiles(state):
    """
    Function that checks for blank cells.
    Returns: a list of blank cells.
    """
    blanks = list()
    for i, row in enumerate(state):
        for j, tile in enumerate(row):
            if not tile:
                blanks.append([i, j])
    
    return blanks

def valid_action(i, j):
    """
    Function checks if an action is valid.
    Returns: True if cell is empty.
    """
    return True if [i, j] in blank_tiles(BOARD) else False

def apply_action(i, j, player):
    """
    Applies an action to the board given the action is valid.
    Returns: None, it just applies an action if it's valid.
    """
    if valid_action(i, j):
        BOARD[i][j] = player
    

def minimax(state, depth, player):
    """
    Minimax implementation.
    Returns: Max or Min for (row, col, score)
    """
    if AGENT:
        """
        If AGENT score is set to -inf
        """
        maximise = [-1 , -1, -inf]
        next_player = HUMAN
    else:
        """
        Else HUMAN and score is set to +inf
        """
        maximise = [-1, -1, +inf]
        next_player = AGENT
    
    if depth == 0 or game_over(state):
        score = eval(state)
        return [-1, -1, score]
    
    for tile in blank_tiles(state):
        i, j = tile[0], tile[1]
        state[i][j] = player
        score = minimax(state, depth - 1, next_player)
        state[i][j] = 0
        score[0], score[1] = i, j

        if AGENT and score[2] > maximise[2]:
            """
            Update Max value
            """
            maximise = score 
        else:
            if score[2] > maximise[2]:
                """
                Update Min value
                """
                maximise = score

        return maximise

def print_board(state, agent_piece, human_piece):
    """
    Prints the current board state.
    Returns: None, just prints to terminal.
    """
    pieces = {
    HUMAN: human_piece,
    AGENT: agent_piece,
    NONE: BLANK
    }
    print(LINE)
    for row in state:
        for tile in row:
            print(f"| {pieces[tile]} |", end='')
        print(LINE)

def agent(agent_piece, human_piece):
    """
    Agent function to call minimax.
    No depth limit mwuahahaha (going to regret this)
    Returns: None, just applies a move.
    """
    depth = len(blank_tiles(BOARD))
    if depth == 0 or game_over(BOARD):
        # GAME OVER
        return None

    print(f"Agent's Turn (Piece: {agent_piece})")
    print_board(BOARD, agent_piece, human_piece)

    """
    Recall that input is: state, depth, player
    """
    move = minimax(BOARD, depth, AGENT)
    apply_action(move[0], move[1], AGENT)

def human(agent_piece, human_piece):
    """
    Human function to apply move.
    Also allows the human to choose piece (X or O)
    Returns: None, just applies a move.
    """
    depth = len(blank_tiles(BOARD))
    if depth == 0 or game_over(BOARD):
        # GAME OVER
        return None
        
    print_board(BOARD, agent_piece, human_piece)
    print(f"Your Turn (Piece: {human_piece})")

    while True:
        action = input("Enter your action (1 - 9): ")
        if action.isdigit() and int(action) in range(1, 9):
            action = int(action)
            try:
                coord = ACTIONS[action]
                apply_action(coord[0], coord[1], HUMAN)
                break # god this is probably bad
            except:
                print("EXCEPT Invalid Action. Try Again")
        else:
            print("Invalid Action. Try Again")

        

    