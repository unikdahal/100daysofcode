import random
import os
from logo_blackjack import logo
cards=[11,2,3,4,5,6,7,8,9,10,10,10]

def calculate_scores(list):
    score=sum(list)
    if score==21 and len(list)==2:
        return 0
    elif 11 in list and score>21:
        list.remove(11)
        list.append(1)
    return sum(list)
def Compare_score(user_score,computer_score):
    if user_score==computer_score:
        return "It's a draw"
    elif computer_score==0:
        return "Lose, Opponent has a blackjack"
    elif user_score==0:
        return "Win with a Blackjack"
    elif user_score>21:
        return "Lose, You went over"
    elif computer_score>21:
        return "Opponent went over, You win"
    elif user_score>computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    my_card=[]
    computer_card=[]
    draw_card=True
    n=3

    while draw_card:
        for i in range(1,n):
            my_card.append(random.choice(cards))
            computer_card.append(random.choice(cards))

        user_score=calculate_scores(my_card)
        computer_score=calculate_scores(computer_card)
        if user_score==0 or computer_score ==0 or user_score>21:
            break

        print(f"Yours cards: {my_card}, current score: {user_score}\n")
        print(f"Computers first card: {computer_card[0]}")

        if input("Type 'y' to get another card, type 'n' to pass")=='y':
                draw_card=True
                n=2
        else:
            draw_card=False

    while computer_score!=0 and computer_score<17:
        computer_card.append(random.choice(cards))
        computer_score=calculate_scores(computer_card)


    print(f'Your final hand is {my_card} and final score is {user_score}')
    print(f'Computer hand is {computer_card} and final score is {computer_score}')
    print(Compare_score(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('clear')
  play_game()
