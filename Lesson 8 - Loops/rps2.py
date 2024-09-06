import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
playagain = True

while playagain:

    playerchoice = input("\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    # Convert player input to an integer
    player = int(playerchoice)

    # Corrected the condition using logical OR (or) and comparing `player` to 1 and 3
    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")    
        
    # Generate a random choice for the computer from the list ['1', '2', '3']
    computerchoice = random.choice(['1', '2', '3'])

    # Convert computer choice to an integer
    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.','') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".\n")

    # if who wins
    if player == 1 and computer == 3:
        print("You win! 🎉")
    elif player == 2 and computer == 1:
        print("You win! 🎉")
    elif player == 3 and computer == 2:
        print("You win! 🎉")
    elif player == computer:
        print("Tie game! 😲")    
    else:
        print("Python win! 🐍")    
    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")
    
    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🍾🥂🎉")    
        print("Thank you for playing\n")
        playagain = False
        # or use a break
        
sys.exit("Bye! 👋🏻")    
    