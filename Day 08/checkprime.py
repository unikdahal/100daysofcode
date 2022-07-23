import math
def primechecker(n):
    count=0
    for i in range(2,round(math.sqrt(n))):
        if(n%i==0):
            count=1
            break
    if(count==1):
        print("It's not a prime number")
    else:
        print("It's a prime number")

n=int(input("Enter the number"))
primechecker(n)
