import random
import json
import os
from pathlib import Path

lifeLeft = 3

scoreData = {
    'game' : []
}

score = Path("score.json")

if not score.exists():
    score.write_text(json.dumps(scoreData, indent = 4))

initial_data = json.loads(score.read_text())

try:
    lowerNum, higherNum = input ("What do you want the range of number to Be: ").split()
    lowerNum = int(lowerNum)
    higherNum = int(higherNum)
except ValueError:
    print("Error: You need to input values like 1 4 or 10 50.")
    exit()
except:
    print("Error: You need to try again.")
    exit()

SECRET_NUMBER = random.randint(lowerNum, higherNum)

while lifeLeft > 0:
    try:
        userGuess = int(input(f"Guess a number between {lowerNum} and {higherNum}:  "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if SECRET_NUMBER == userGuess:
        print(f"Congrats!! You Guessed the Secret Number {userGuess}")
        initial_data["game"].append({'result' : 'win'})
        break
    else:
        lifeLeft -= 1
        print(f"Wrong, You have {lifeLeft} left.")

if lifeLeft == 0:
    print(f"Sorry, You don't have any Life left. \nThe Secret Number was {SECRET_NUMBER}")
    initial_data["game"].append({'result' : 'loss'})
    
with open(score, "w") as f:
    f.write(json.dumps(initial_data , indent = 4))