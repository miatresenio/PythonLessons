import sys
import random
from enum import Enum

# example of recursion

def play_rps():
    
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
        

    playerchoice = input("\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
    
    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    # Convert player input to an integer
    player = int(playerchoice)

        
    # Generate a random choice for the computer from the list ['1', '2', '3']
    computerchoice = random.choice(['1', '2', '3'])

    # Convert computer choice to an integer
    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.','').title() + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.','').title() + ".\n")

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
        
    print("\nPlay again?")     
    
    while True:
        playagain = input("\nY for Yes or \nQ to Quit \n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break
    
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🍾🥂🎉")    
        print("Thank you for playing\n")
        sys.exit("Bye! 👋🏻") 
        # or use a break
        

play_rps()    