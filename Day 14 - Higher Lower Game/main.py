import random
from art import logo, vs
from game_data import data
from replit import clear
"""
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },]
"""

def print_view(a, b):
    """Display interface"""
    print(f"Compare A : {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B : {b['name']}, a {b['description']}, from {b['country']}.")

def compare(a, b, answer):
    """Compare whether the answer is correct"""
    #print(a['follower_count'] , b['follower_count'])
    if answer == 'A' and a['follower_count'] > b['follower_count']:
        return True
    elif answer == 'B' and b['follower_count'] > a['follower_count']:
        return True
    else:
        return False

def game():
    score = 0
    game_flag = False
    while not game_flag:
        print(logo)
        if score != 0:
            print(f"You're right! Current score: {score}.")
        random_data_a = random.choice(data)
        random_data_b = random.choice(data)
        while random_data_a == random_data_b:
            random_data_b = random.choice(data)  
        print_view(random_data_a, random_data_b)
        answer = input("Who has followers? Type 'A' or 'B': ")
        #print(compare(random_data_a, random_data_b, answer))
        if compare(random_data_a, random_data_b, answer):
            score += 1
        else:
            game_flag = True
        clear()
    else:
        print(logo)
        print(f"Sorry, that's wrong. Fial score: {score}")
game()