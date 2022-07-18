import random

names_string=input("Enter the name of everyone separated by comma.")
names=names_string.split(",")
a=random.randint(0,len(names)-1)
print(f'{names[a]} will pay the bills')
