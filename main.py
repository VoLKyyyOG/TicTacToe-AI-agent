"""
Minimax implementation for Tic Tac Toe
Author: Akira Wang
"""
# Import Dependencies
from algorithms import *

def main():
    """
    Main function.
    """
    system('cls')

    human_piece = False
    while not human_piece: # Originally defined as '' so it should be None
        print("X goes first, and O goes second.")
        choice = input("Choose X or O: ").upper()
        if choice in 'XO':
            human_piece = choice
            if choice == 'X':
                agent_piece = 'O'
            else:
                agent_piece = 'X'
            print("Successful. Let's start the game!")
        else:
            print("Invalid Piece. Try Again.")

    if choice == 'O':
        """
        If human decides to go second, run the agent first.
        """
        agent(agent_piece, human_piece)
    
    while len(blank_tiles(BOARD)) > 0 and not game_over(BOARD):
        """
        Resume playing.
        """
        human(agent_piece, human_piece)
        agent(agent_piece, human_piece)
    
    system('cls')

    if winner(BOARD, HUMAN):
        print("YOU WIN!")
        print_board(BOARD, agent_piece, human_piece)
    elif winner(BOARD, AGENT):
        print("You muppet, you've lost :(")
        print_board(BOARD, agent_piece, human_piece)
    else:
        print("DRAW!")
        print_board(BOARD, agent_piece, human_piece)
    
    exit()

if __name__ == '__main__':
    main()