import random

print('Welcome to Coin Toss Game')
a=input('Enter your prediction. Type "head" or "tail"').lower()
no=random.randint(1, 2)

if(no==1 and a=='head'):
    print('It is head and You Won')
elif(no==1 and a=='tail'):
    print('It is head and you lost.Better luck next time')
elif(no==2 and a=='head'):
    print('It is tail and You lost.Better luck next time')
else:
    print('It is tail and you Won')
