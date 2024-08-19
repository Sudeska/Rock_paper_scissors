
import random
rps_list = ["rock", "paper", "scissors"]

game_start = input("Do you wish to start?").lower()

player_score = 0
player_game_score = 0
computer_score = 0
computer_game_score = 0


def rps_game():

    global player_score, computer_score, player_game_score, computer_game_score

    while computer_score < 2 and player_score < 2:

        player_choice = input("Rock, paper or scissors?\n").lower()

        computer_choice = random.choice(rps_list)

        while player_choice not in rps_list:
            print("Please type your choice correctly!")
            player_choice = input("Rock, paper or scissors?").lower()

        if player_choice == computer_choice:
            print("It is a draw!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "paper" and computer_choice == "rock") or \
                (player_choice == "scissors" and computer_choice == "paper"):
            print("You've won the round!")
            player_score += 1
        else:
            print("You've lost the round!")
            computer_score += 1
        print(f"Player's score: {player_score}, computer's score: {computer_score}")

    if player_score == 2:
        print("You've won the game!\n")
        player_game_score += 1

    if computer_score == 2:
        print("Computer won!")
        computer_game_score += 1

    print(f"Final scores: Player = {player_game_score} - Computer =  {computer_game_score}")

    player_score = 0
    computer_score = 0

    restart_player = input("Do you wish to play again?").lower()

    restart_computer = random.choice(["yes", "no"])

    if restart_player == "yes" and restart_computer == "yes":
        rps_game()
    if restart_player != "yes" and "no":
        print("Please type 'yes' or 'no'.")
    if restart_computer == "no":
        print("Sorry, computer does not want to play :( .")


if game_start == "yes":
    rps_game()