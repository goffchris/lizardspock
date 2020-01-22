# Set up. Import random function and establish winner variable

import random

winner = ''

# List of possible choices. Computer chooses

choices = ['rock','paper','scissors','lizard','spock']

computer_choice = random.choice(choices)

# Input user choice

user_choice = input('rock, paper, scissors, lizard or spock? ')

# Evaluate winner using game logic. If same, tie. Sets conditions of computer winning. No need to fully define user wins

if computer_choice == user_choice:
    winner = 'Tie'

elif computer_choice == 'rock' and user_choice == 'scissor' or user_choice == 'lizard':
    winner = 'Computer'

elif computer_choice == 'paper' and user_choice == 'rock' or user_choice == 'spock':
    winner = 'Computer'

elif computer_choice == 'scissor' and user_choice == 'paper' or user_choice == 'lizard':
    winner = 'Computer'

elif computer_choice == 'lizard' and user_choice == 'paper' or user_choice == 'spock':
    winner = 'Computer'

elif computer_choice == 'spock' and user_choice == 'scissor' or user_choice == 'rock':
    winner = 'Computer'


else:
    winner = 'User'

# Gives results of tie or who won

if winner == 'Tie':
    print('The computer chose', computer_choice,'and the user chose', user_choice)

    print('It is a tie!')

else:
    print('The computer chose', computer_choice,'and the user chose', user_choice)

    print('The winner is', winner, '!')
