def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def Calculator():
    no1=float(input("What's the first number?\n"))
    otheroperation=True
    while otheroperation:
        operation=input("What operation you want to perform?\n+\n-\n*\n/\n")
        no2=float(input("What's the next number\n"))
        function=operations[operation]
        result=function(no1,no2)
        print(result)
        moreoperation=input(f"Type 'y' to continue calculating with the {result} or type 'n' to start over or type 'e' to exit")
        if moreoperation=="y":
            no1=result
        elif moreoperation=="e":
            break
        else:
            otheroperation=False
            Calculator()
Calculator()
