from game import Game

def get_user_menu_choice():
    """
    Display menu and get user choice
    Returns: string representing user's choice
    """
    print("\n==== MENU ====")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    
    choice = input("Please select an option (1-3): ")
    return choice

def print_results(results):
    """
    Print game results in a user-friendly format
    Parameters:
        results: dictionary containing game statistics
    """
    print("\n==== GAME RESULTS ====")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print(f"Total games played: {sum(results.values())}")
    print("\nThank you for playing! Hope to see you again soon!")

def main():
    """
    Main game loop and program control
    """
    # Initialize results dictionary
    results = {
        'win': 0,
        'loss': 0,
        'draw': 0
    }
    
    while True:
        # Get user menu choice
        choice = get_user_menu_choice()
        
        if choice == '1':
            # Play a new game
            game = Game()
            result = game.play()
            results[result] += 1
            
        elif choice == '2':
            # Show current scores
            print_results(results)
            
        elif choice == '3':
            # Quit game and show final results
            print("\n=== FINAL RESULTS ===")
            print_results(results)
            break
            
        else:
            print("\nInvalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    main()