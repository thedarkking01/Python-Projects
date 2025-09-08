import random
from game_logic import determine_winner
from player import get_user_input
from Rock_paper_scissor.computer import get_computer_choice
EMOJI_MAP={'rock':'✊','paper':'👋','scissors':'✌️'}
def get_emoji(choice):
    return EMOJI_MAP.get(choice)
def welcome_user():

    print('Welcome to Rock, Paper, Scissors!')

welcome_user()

valid_choices=['rock','paper','scissors']



user_choice = get_user_input(valid_choices)


computer_choice=get_computer_choice(valid_choices)

print(f"You chose: {get_emoji(user_choice)}")

print(f"Computer chose: {get_emoji(computer_choice)}")

