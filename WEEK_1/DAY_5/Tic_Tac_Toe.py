def display_board(board):
    """Display the current state of the board"""
    print('\n' * 2)
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print('\n')

def player_input(player, board):
    """Get and validate player input"""
    while True:
        try:
            position = int(input(f'Player {player}, choose a position (1-9): ')) - 1
            if 0 <= position <= 8 and board[position] == ' ':
                return position
            else:
                print("Invalid position. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def check_win(board):
    """Check if there's a winner"""
    # Winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return False

def check_tie(board):
    """Check if the game is a tie"""
    return ' ' not in board

def play():
    """Main game function"""
    # Initialize the board
    board = [' ' for _ in range(9)]
    current_player = 'X'
    game_over = False
    
    # Welcome message
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered from 1-9, left to right, top to bottom.")
    
    # Main game loop
    while not game_over:
        # Display current board
        display_board(board)
        
        # Get player input
        position = player_input(current_player, board)
        
        # Update board
        board[position] = current_player
        
        # Check for win
        if check_win(board):
            display_board(board)
            print(f'Player {current_player} wins! 🎉')
            game_over = True
        
        # Check for tie
        elif check_tie(board):
            display_board(board)
            print("It's a tie! 🤝")
            game_over = True
        
        # Switch players
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    
    # Ask to play again
    if input("Play again? (y/n): ").lower().startswith('y'):
        play()

# Start the game
if __name__ == "__main__":
    play()