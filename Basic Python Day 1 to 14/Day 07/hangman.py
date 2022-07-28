
import random
import word_list
import hangman_art

print(hangman_art.logo)
print("Welcome to Hangman")
wordlist= word_list.word_list1
chosen_word=random.choice(wordlist)
lives=6
blank=[]
stages= hangman_art.stages
for i in chosen_word:
    blank.append('_')

end_of_game=False
print(stages[lives])
while not end_of_game:

    guess=input('Enter the letter').lower()

    for i in range(0,len(chosen_word)):
        if(guess==chosen_word[i]):
            blank[i]=guess
        if guess not in chosen_word:
            print("You lost a live")
            lives-=1
            print(stages[lives])
            break

    print(' '.join(blank))
    if(lives<1):
        print("You lose")
        end_of_game=True

    if "_" not in blank:
        end_of_game= True
        print("You Win")
