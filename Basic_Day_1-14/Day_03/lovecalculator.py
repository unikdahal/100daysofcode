#Love Calculator

first_name=input('Enter your name').lower()
second_name=input('Enter your partner name').lower()

fullname=first_name+second_name

true_count=0
true_count+=fullname.count('t')
true_count+=fullname.count('r')
true_count+=fullname.count('u')
true_count+=fullname.count('e')
love_count=0
love_count+=fullname.count('l')
love_count+=fullname.count('o')
love_count+=fullname.count('v')
love_count+=fullname.count('e')
total_score=true_count*10+love_count

if(total_score<10 or total_score>90):
    print(f'Your score is {total_score}, you go together like coke and mentos')
elif(total_score<=50 and total_score>=40):
    print(f'Your score is {total_score}, you are alright together')
else:
    print(f'Your score is {total_score}')
