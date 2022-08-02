print('Welcome to Python Pizza Deliveries')
size=input('What size pizza do you want? S,M or L')
add_pepperoni=input('Do you want to add pepperoni? Y or N')
extra_cheese=input('Do you want extra cheese?Y or N')

if(size=='S'):
    total=15
    if(add_pepperoni=='Y'):
        total+=2
elif(size=='M'):
    total=20
    if(add_pepperoni=='Y'):
        total+=3
else:
    total=25
    if(add_pepperoni=='Y'):
        total+=3

if(extra_cheese=='Y'):
    total+=1

print(f'Your total bill is {total}')
