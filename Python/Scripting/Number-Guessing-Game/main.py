import random
import json
import os
from pathlib import Path

lifeLeft = 3

cwd = os.getcwd()
score = Path(os.path.join(cwd, "score.json"))

if(score.exists() != True):
    Path(score).write_text('{}')

try:
    lowerNum, higherNum = input ("What do you want the range of number to Be: ").split()
except ValueError:
    print("Error: You need to input values like 1 4 or 10 50.")
    exit()
except:
    print("Error: You need to try again.")
    exit()

SECRET_NUMBER = random.randint(int(lowerNum), int(higherNum) + 1)

while lifeLeft != 0:
    userGuess = int(input(f"Guess a number between {lowerNum} and {higherNum}:  "))
    
    if SECRET_NUMBER == userGuess:
        print(f"Congrats!! You Guessed the Secret Number {userGuess}")
        break
    else:
        lifeLeft -= 1
        print(f"Wrong, You have {lifeLeft} left.")
    
if lifeLeft == 0:
    print(f"Sorry, You don't have any Life left. \nThe Secret Number was {SECRET_NUMBER}")
