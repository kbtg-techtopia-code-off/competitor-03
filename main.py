# implement rock paper scissors lizard and spock game
import random

# function to get user input
def get_user_input():
    while True:
        print("Choose your option: ")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Lizard")
        print("5. Spock")
        user_input = input("Please input your choice >>> ")
        if user_input == '1':
            return 'rock'
        elif user_input == '2':
            return 'paper'
        elif user_input == '3':
            return 'scissors'
        elif user_input == '4':
            return 'lizard'
        elif user_input == '5':
            return 'spock'
        else :
            print("Invalid input, please try again")
        print("==============================\n")
        
def get_computer_input():

    # random string rock paper scissors
    computer_input = random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])
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

    # All cases that user wins

    # user choose rock and computer choose scissors or lizard
    if user_input == 'rock' and computer_input in ['scissors', 'lizard']:
        user_win = True
        player_score += 1

    # user choose paper and computer choose rock or spock   
    elif user_input == 'paper' and computer_input in ['rock', 'spock']:
        user_win = True
        player_score += 1

    # user choose scissors and computer choose paper or lizard
    elif user_input == 'scissors' and computer_input in ['paper', 'lizard']:
        user_win = True
        player_score += 1

    # user choose lizard and computer choose paper or spock
    elif user_input == 'lizard' and computer_input in ['paper', 'spock']:
        user_win = True
        player_score += 1

    # user choose spock and computer choose rock or scissors 
    elif user_input == 'spock' and computer_input in ['rock', 'scissors']:
        user_win = True
        player_score += 1

    # All cases that computer wins
    elif computer_input == 'rock' and user_input in ['scissors', 'lizard']:
        computer_score += 1

    # user choose paper and computer choose rock or spock   
    elif computer_input == 'paper' and user_input in ['rock', 'spock']:
        computer_score += 1

    # user choose scissors and computer choose paper or lizard
    elif computer_input == 'scissors' and user_input in ['paper', 'lizard']:
        computer_score += 1
    # user choose lizard and computer choose paper or spock
    elif computer_input == 'lizard' and user_input in ['paper', 'spock']:
        computer_score += 1
    # user choose spock and computer choose rock or scissors 
    elif computer_input == 'spock' and user_input in ['rock', 'scissors']:
        computer_score += 1
        
    
    count+=1
    print("The computer choice: ", computer_input)
    print("The player choice: ", user_input)
    print("The winner is:", "player" if user_win else "computer")
    print("Wins: ", player_score)
    print("Losses: ", computer_score)
    print("Games passed: ", count)
    print("==============================\n")


    