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
from os import system
from time import sleep

# Global Variables
BOARD = [
    [0, 0 ,0],
    [0, 0, 0],
    [0, 0, 0]
]

ACTIONS = {
    0: [0, 0], 1: [0, 1], 2: [0, 2],
    3: [1, 0], 4: [1, 1], 5: [1, 2],
    6: [2, 0], 7: [2, 1], 8: [2, 2],
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
        return True
    else:
        False

def minimax(state, depth, player):
    """
    Minimax implementation.
    Returns: Max or Min for (row, col, score)
    """
    if player == AGENT:
        maximise = [-1, -1, -inf]
    else:
        maximise = [-1, -1, +inf]

    if depth == 0 or game_over(state):
        score = eval(state)
        return [-1, -1, score]

    for tile in blank_tiles(state):
        i, j = tile[0], tile[1]
        state[i][j] = player
        score = minimax(state, depth - 1, -player)
        state[i][j] = 0
        score[0], score[1] = i, j

        if player == AGENT:
            """
            Max Value
            """
            if score[2] > maximise[2]:
                maximise = score
        else:
            """
            Min Value
            """
            if score[2] < maximise[2]:
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

    system('cls')

    print_board(BOARD, agent_piece, human_piece)
    print(f"Agent's Turn (Piece: {agent_piece})")
    

    """
    Recall that input is: state, depth, player
    """
    move = minimax(BOARD, depth, AGENT)
    apply_action(move[0], move[1], AGENT)

    sleep(0.5)

def human(agent_piece, human_piece):
    """
    Human function to apply move.
    Returns: None, just applies a move.
    """
    depth = len(blank_tiles(BOARD))
    if depth == 0 or game_over(BOARD):
        # GAME OVER
        return None

    system('cls')

    print_board(BOARD, agent_piece, human_piece)
    print(f"Your Turn (Piece: {human_piece})")

    while True:
        action = input("Enter your action (0 - 8): ")
        if action.isdigit() and int(action) in range(9):
            action = int(action)
            # This is probably a bad hotfix but it doesnt work 
            # sometimes if its not like this hmmm
            try:
                coord = ACTIONS[action]
                if apply_action(coord[0], coord[1], HUMAN):
                    break
                else:
                    print("Invalid Action. Try Again")
            except:
                print("Invalid Action. Try Again")
        else:
            print("Invalid Action. Try Again")