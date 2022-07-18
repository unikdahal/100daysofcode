#Rock Paper Scissor Game

import random

choice1=int(input('What do you choose?Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))

choice2=random.randint(0, 2)

if(choice1==0):
    print('You choose Rock ✊\n')
elif(choice1==1):
    print('You choose Paper ✋ \n')
else:
    print('You choose Scissors ✂️ \n')

if(choice2==0):
    print('Bot choose Rock ✊\n')
elif(choice2==1):
    print('Bot choose Paper ✋\n')
else:
    print('Bot choose Scissors ✂️\n')

if(choice1==choice2):
    print("It's a draw")
elif(choice1==0 and choice2==2):
    print('Congratulations you beat the bot')
elif(choice1==0 and choice2==1):
    print('Looser You lost a bot')
elif(choice1==1 and choice2==0):
    print('Congratulations you beat the bot')
elif(choice1==1 and choice2==2):
    print('Looser You lost a bot')
elif(choice1==2 and choice2==1):
    print('Congratulations you beat the bot')
else:
    print('Looser You lost a bot')
