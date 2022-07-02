#TIP Calculator

total=float(input("What was the total bill?\n"))
people=int(input('How many people to split the bill?\n'))
percentage=int(input("What percentage of tip would you like to give?"))

total=total+(percentage*total/100)
eachPerson=round(total/people,2)

print(f'Each person should pay ${eachPerson}')
