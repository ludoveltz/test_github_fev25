import random

class Game:
    def __init__(self):
        """Initialize the game with valid choices"""
        self.valid_items = ['rock', 'paper', 'scissors']

    def get_user_item(self):
        """Ask user to select an item and validate the input"""
        while True:
            user_choice = input("Select an item (rock/paper/scissors): ").lower()
            if user_choice in self.valid_items:
                return user_choice
            print("Invalid choice! Please select rock, paper, or scissors.")

    def get_computer_item(self):
        """Randomly select an item for the computer"""
        return random.choice(self.valid_items)

    def get_game_result(self, user_item, computer_item):
        """
        Determine the game result
        Returns: 'win', 'draw', or 'loss'
        """
        if user_item == computer_item:
            return 'draw'

        winning_combinations = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }

        return 'win' if winning_combinations[user_item] == computer_item else 'loss'

    def play(self):
        """
        Play one game round
        Returns: game result as string ('win', 'draw', or 'loss')
        """
        # Get user and computer items
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()

        # Get game result
        result = self.get_game_result(user_item, computer_item)

        # Display game outcome
        print(f"\nYou selected {user_item}.")
        print(f"The computer selected {computer_item}.")
        
        # Print result message
        result_messages = {
            'win': 'You win!',
            'draw': 'You drew!',
            'loss': 'You lose!'
        }
        print(result_messages[result])

        return result