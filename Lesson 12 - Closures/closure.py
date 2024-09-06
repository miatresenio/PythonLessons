# Closure - is s function having access to the scope of its parent function
# after the parent function has returned.
# Nested function - is going to have access to the scope of it's parent 
# function.

 # The Nested function will always have access to the variable value that is in the parent function.

def parent_function(person, coins):
   # coins = 3      
    
    def play_game():
        nonlocal coins
        coins -= 1
        
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")  
        else:
             print("\n" + person + " is out of coins.") 
             
    return play_game        # When we return this, then the closure is created in playgame                          

mia = parent_function("Mia", 3)
myca = parent_function("Myca", 5)
   
mia()              
mia()              
          
myca()     

mia()         

# closure is created when the parent function returns,