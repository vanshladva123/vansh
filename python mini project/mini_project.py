import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "stone" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "stone"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def stone_paper_scissors():
    print("Welcome to the Stone-Paper-Scissors game!")
    
    # List of possible choices
    choices = ["stone", "paper", "scissors"]
    
    while True:
        # Get player's choice
        player_choice = input("Enter your choice (stone, paper, scissors) or 'quit' to exit: ").lower()
        
        # Allow player to quit the game
        if player_choice == "quit":
            print("Thanks for playing!")
            break
        
        # Check if player's input is valid
        if player_choice not in choices:
            print("Invalid input! Please choose from 'stone', 'paper', or 'scissors'.")
            continue
        
        
        # Get computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        print()

stone_paper_scissors()