import random
from tkinter.tix import ExFileSelectBox 
print("Guessing Number")
number = random.randint(1,9)
chances = 0
print("Guessing A Number Between 1 and 9")
while chances < 5:
    guess = int(input("enter your guess-"))
    if guess == number:
        print("coungrates")
        break
    elif guess<number:
        print("your guess was to low",guess)
    else:
        print("guess was to high",guess)
    chances += 1
if not chances <5 :
    print("you lose",number)


