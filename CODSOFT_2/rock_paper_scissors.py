import random

def get_user_choice():
    """
    Prompt the user to choose rock, paper, or scissors.
    """
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    """
    Generate a random choice (rock, paper, or scissors) for the computer.
    """
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on the user's choice and the computer's choice.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """
    Play a round of Rock-Paper-Scissors.
    """
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose {user_choice}.")
    print(f"The computer chose {computer_choice}.\n")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
    while input("Do you want to play again? (yes/no): ").lower() == 'yes':
        play_game()
