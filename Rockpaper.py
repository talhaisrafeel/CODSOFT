import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("1. Rock\n2. Paper\n3. Scissors\n4. Quit")

        user_choice_index = input("Enter your choice (1-3): ")
        
        if user_choice_index == '4':
            print("Thanks for playing. Final Scores:")
            print(f"You: {user_score}  Computer: {computer_score}")
            break

        if user_choice_index not in ['1', '2', '3']:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        user_choice = ["rock", "paper", "scissors"][int(user_choice_index) - 1]
        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"\nYou chose {user_choice}")
        print(f"Computer chose {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Scores - You: {user_score}  Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
