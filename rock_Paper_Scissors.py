#Rock-Paper-Scissor Game
import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors'):
       return 'User'
    elif (user_choice == 'paper' and computer_choice == 'rock'):
        return 'User'
    elif (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'User'
    else:
        return 'Computer'

def main():
    print('''       Rock-Paper-Scissors
             Game''')
    print("------------------------------------------------")

    user_score = 0
    computer_score = 0

    while True:
        print("Options: rock, paper, scissors")
        user_choice = input("Enter your choice [type 'exit' to quit]: ").lower()

        if user_choice == 'exit':
            print(f"\nFinal Score: User {user_score} - Computer {computer_score}")
            print("Thank you for playing!")
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("\nInvalid choice!")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer choice: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        
        if winner == 'User':
            print("------------------------------------")
            print("\nYou win this round...")
            user_score += 1
        elif winner == 'Computer':
            print("--------------------------------------")
            print("\nComputer wins this round...")
            computer_score += 1
        else:
            print("----------------------------------------")
            print("\nIt's a draw!")

        print(f"\nScore: User {user_score} - Computer {computer_score}")
        print("------------------------------------------------------------")

if __name__ == "__main__":
    main()
