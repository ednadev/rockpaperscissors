import random

while True:

    user_action = input("Which do you choose? 'r', 'p', or 's': ")
    possible_actions = ["r", "p", "s"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        keep_playing = print("Would you like to play again? 'y' or 'n'\n")

    elif user_action == "r":
        if computer_action == "s":
            print("You win! Rock beats scissors!")

        else:
            print("You lose! Paper beats rock.")

    elif user_action == "p":
        if computer_action == "r":
            print("You win! Paper beats rock!")

        else:
            print("You lose! Scissors beats paper.")

    elif user_action == "s":
        if computer_action == "p":
            print("You win! Scissors beats paper!")
        else: 
            print("You lose! Rock beats scissors.")

    if user_action not in possible_actions:
        print("Error! Wrong input, try again.")
    