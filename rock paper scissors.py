import random

def print_instructions():
    print('Winning Rules of the game ROCK PAPER SCISSORS are:\n'
          'Rock vs Paper -> Paper Wins\n'
          'Rock vs Scissors -> Rock Wins\n'
          'Paper vs Scissors -> Scissors Wins\n')

def get_user_choice():
    while True:
        try:
            print("Enter your choice \n1 - Rock\n2 - Paper\n3 - Scissors")
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter a valid number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_choice_name(choice):
    choices = ['Rock', 'Paper', 'Scissors']
    return choices[choice - 1]

def get_winner(user_choice_name, comp_choice_name):
    if user_choice_name == comp_choice_name:
        return "DRAW"
    elif (user_choice_name == 'Rock' and comp_choice_name == 'Scissors') or \
         (user_choice_name == 'Paper' and comp_choice_name == 'Rock') or \
         (user_choice_name == 'Scissors' and comp_choice_name == 'Paper'):
        return "User"
    else:
        return "Computer"

def play_game():
    user_choice = get_user_choice()
    user_choice_name = get_choice_name(user_choice)
    print("User choice is:", user_choice_name)
    
    print("Now it's Computer's Turn...")
    comp_choice = random.randint(1, 3)
    comp_choice_name = get_choice_name(comp_choice)
    print("Computer choice is:", comp_choice_name)

    print(user_choice_name, "vs", comp_choice_name)

    winner = get_winner(user_choice_name, comp_choice_name)

    if winner == "DRAW":
        print("<== It's a tie! ==>")
    elif winner == "User":
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

def main():
    print_instructions()
    while True:
        play_game()
        ans = input("Do you want to play again? (Yes/No): ").lower()
        if ans == 'no':
            print("Thanks for playing!")
            break

main()