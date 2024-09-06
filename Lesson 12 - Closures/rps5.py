import sys
import random
from enum import Enum

# example of closure

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0
    
    def play_rps():
        nonlocal player_wins 
        nonlocal python_wins
        
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
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "You win! 🎉"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "You win! 🎉"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "You win! 🎉"
            elif player == computer:
                return "Tie game! 😲"    
            else:
                python_wins += 1
                return "Python win! 🐍"   
            
        game_result = decide_winner(player, computer)   
        
        print(game_result) 
            
        nonlocal game_count
        game_count += 1
        
        print("\nGame count: "+ str(game_count))    
        print("\nPlayer wins: "+ str(player_wins))    
        print("\nPython wins: "+ str(python_wins))    
            
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
        
    return play_rps

play = rps()    

play()