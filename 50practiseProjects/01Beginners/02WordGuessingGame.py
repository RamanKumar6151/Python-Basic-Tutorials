import os
from random import choice

os.system("cls")

words=["lumos", "nox", "avadakedvra", "accio", "patronus"]
word=choice(words)
print("guess character")
guesses=""
turns=12
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_")
            failed+=1
    if failed==0:
        print("win")
        break
    print()
    guess=input("enetr guess ")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("wrong")
        print(f"you have {turns} turns")
    if(turns==0):
        print("you lose")