# number guessing game v1
# user predicts the number given by computer

from os import system
from random import randint
from math import log

system("cls")

lower=int(input("Lower Bound="))
upper=int(input("Upper Bound="))

x=randint(lower, upper)
# print(f"\ntest {x}\n")
# print(x)
chances=round(log(upper-lower+1,2))  # base 2

# count=0

print(f"ATTENTION!!! you have {chances} chances")
# guess the number
while(chances>0):
    chances=chances-1
    guess=int(input("\nGuess the number="))
    if(guess==x):
        print("You guesssed it correct")
        break
    elif(guess>x):
        print("Guessed too high")
        if(chances>0):
            print(f"WARNING!!!! only {chances} chances left\n")
        else:
            print("ATTENTION!!!!! no chances left\n")
    else:
        print("You guessed  too low")
        if(chances>0):
            print(f"WARNING!!!! only {chances} chances left\n")
        else:
            print("ATTENTION!!!!! no chances left\n")
else:
    print(f"Better luck next time x={x}")
