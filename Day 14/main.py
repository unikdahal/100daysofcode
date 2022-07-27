from game_data import data
import art
import random
import os


def runGame():
    isALive=True
    choice1=random.randint(0, len(data)-1)
    score=0

    while isALive:
        choice2=random.randint(0, len(data)-1)
        print(art.logo)

        if(choice1==choice2):
            choice2=random.randint(0, len(data)-1)

        print(f"Your score is {score}")

        print("Compare A:" + (data[choice1])['name']+", "+(data[choice1])['description']+", from "+(data[choice1])['country'])

        print(art.vs)

        print("Compare B:" + (data[choice2])['name']+", "+(data[choice2])['description']+", from "+(data[choice2])['country'])

        user_choice=input("Who has more followers? Type 'A' or 'B'").upper()

        if(user_choice=="A" and (data[choice1])['follower_count']>(data[choice2])['follower_count']):
            score+=1
            os.system('clear')
        elif(user_choice=="B" and (data[choice2])['follower_count']>(data[choice1])['follower_count']):
            score+=1
            os.system('clear')
        else:
            return score

        choice1=choice2

print(f"Game Over Your Score is {runGame()}")
