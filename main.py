from art import logo, vs
from game_data import data
import random

current_score = 0


def compare_player(a,b,score,ran_player):
    final_score = 0
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == 'a':
        if a > b:
            score = score + 1
            #clear statement
            print(f"You guessed it right, Current Score: {score}")
            random_player(current_score = score,player_b = ran_player)
        elif a < b:
            final_score = score
            print(f"You Lose Your Final Score: {final_score}")
            return
        else:
            print(f"That's a draw")
            return
    elif user_choice == 'b':
        if b > a:
            score = score + 1
            #clear statement
            print(f"You guessed it right, Current Score: {score}")
            random_player(current_score = score,player_b = ran_player)
        elif b < a:
            final_score = score
            print(f"You Lose Your Final Score: {final_score}")
            return
        else:
            print(f"That's a draw")
            return
        

def random_player(current_score, player_b):
    print(logo)
    random_player_A = player_b
    name_A = random_player_A["name"]
    description_A = random_player_A["description"]
    country_A = random_player_A["country"]
    follower_count_A = int(random_player_A["follower_count"])
    print(f"Compare A: {name_A},a {description_A},from {country_A}")
    print(vs)
    random_player_B = random.choice(data)
    name_B = random_player_B["name"]
    description_B = random_player_B["description"]
    country_B = random_player_B["country"]
    follower_count_B = int(random_player_B["follower_count"])
    print(f"Against B: {name_B},a {description_B},from {country_B}")
    compare_player(a = follower_count_A,b = follower_count_B,score = current_score,ran_player = random_player_B)
random_b = random.choice(data)
random_player(current_score = current_score, player_b = random_b)