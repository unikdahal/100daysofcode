#Treasure Island

print('Welcome to Treasure Island\n Your mission is to find the treasure')

choice1=input('You are at a cross road Do you want to go left or right? Type "left" or "right"').lower()

if(choice1=='left'):
    choice2=input('You have a river ahead. Do you want to swim or wait for the boat? Type "swim" or "wait"').lower()
    if(choice2=='wait'):
        choice3=input('You have 3 doors ahead red blue or yellow Choose one door. Type "red" "blue" or "yellow"').lower()
        if(choice3=='yellow'):
            print('Congratulations You have successfully found the treasure.')
        elif(choice3=='red'):
            print('Game Over. There is fire in the room')
        else:
            print('Game Over. There is water in the room')
    else:
        print('Game Over. Crocodile ate you')
else:
    print('Game Over You fell into the hole')
