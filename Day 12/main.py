#Number Guessing Game

import random

print("Welcome to the Number Guessing Game:\n")
print("I'm thinking of a number between 1 and 100m\n")

if input("Choose a Difficulty.Type 'easy' or 'hard").lower()=="easy":
    guess_count=10
else:
    guess_count=5

number=random.randint(1, 100)
won=False
while(guess_count>0):
    guess_number=int(input("Make a guess"))
    if guess_number==number:
        print(f"Congratulations You have won the game . The number was {number}")
        won=True
        break
    if guess_number<number:
        print("Too low")
    else:
        print("Too High")
    guess_count-=1
    print(f"You have {guess_count} guesses remaining")

if guess_count==0 and not won:
    print(f"You have run out of guesses . The number was {number}")
