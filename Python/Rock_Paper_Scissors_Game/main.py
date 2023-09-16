import os
import random

from art import *


def game():
    game_images = [rock, paper, scissors]

    user_score = 0
    computer_score = 0
    should_continue = True

    while should_continue:
        user_choice = int(input("⏳What do you choose?🤔 Type 0 for Rock🌋, 1 for Paper🧻, or 2 for Scissors✂️.\n"))

        if user_choice >= 3 or user_choice < 0:
            print("You typed an invalid number❌, you lose!😔")
        else:
            print("You choose:")
            print(game_images[user_choice])

            computer_choice = random.randint(0, 2)
            print("Computer choose:")
            print(game_images[computer_choice])

            if user_choice == 0 and computer_choice == 2:
                user_score += 1
                print("You win!😃")
            elif computer_choice == 0 and user_choice == 2:
                computer_score += 1
                print("You lose!😭")
            elif computer_choice > user_choice:
                computer_score += 1
                print("You lose!😭")
            elif user_choice > computer_choice:
                user_score += 1
                print("You win!😃")
            else:
                print("It's a draw😎")

            print("User Score:", user_score)
            print("Computer Score:", computer_score)

        next_round = input("🔄Do you want to play another round?🎮 (Yes/No): ").lower()

        if next_round != 'yes':
            print("Goodbye👋🏻, try again!!!🙂")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')


game()
