# implement rock paper scissors game

import random

# function to get user input
def get_user_input():
    while True:
        user_input = input("Please input your choice >>> ")
        if user_input not in ['rock', 'paper', 'scissors']:
            print("Invalid input, please try again")
        else:
            return user_input
        print("==============================\n")
        
def get_computer_input():

    # random string rock paper scissors
    computer_input = random.choice(['rock', 'paper', 'scissors'])
    return computer_input

count = 0
player_score = 0
computer_score = 0
while True:
    user_win = False
    computer_win = False
    user_input = get_user_input()
    computer_input = get_computer_input()

    if user_input == computer_input:
        continue

    # computer choose rock and player choose paper'
    elif computer_input == 'rock' and user_input == 'paper':
        player_score+=1
        user_win = True

    # computer choose rock and player choose scissors
    elif computer_input == 'rock' and user_input == 'scissors':
        computer_score+=1
        computer_win = True

    # computer choose paper and player choose rock
    elif computer_input == 'paper' and user_input == 'rock':
        computer_score+=1
        computer_win = True

    # computer choose scissors and player choose paper
    elif computer_input == 'scissors' and user_input == 'paper':
        computer_score+=1
        computer_win = True

    # computer choose paper and player choose scissors
    elif computer_input == 'paper' and user_input == 'scissors':
        player_score+=1
        user_win = True

    # computer choose scissors and player choose rock
    elif computer_input == 'scissors' and user_input == 'rock':
        player_score+=1
        user_win = True

    count+=1
    print("The computer choice: ", computer_input)
    print("The player choice: ", user_input)
    print("The winner is:", "player" if user_win else "computer")
    print("Wins: ", player_score)
    print("Losses: ", computer_score)
    print("Games passed: ", count)
    print("==============================\n")


    