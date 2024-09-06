# Global Scope

name = "Mia"
count = 1


   
# Nested Function -  only going to use the function inside of the other function &
# therefore it dsnt need to define outside of the function

def another():
    color = "blue"
    global count 
    count += 1
    print(count)
     
    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)
        
    greeting("Mia")
    
        
another()    

# We can call one function inside of the local scope of another function and that's bc
#  this function greeting was defined in the global scope so it's available to be called
#  inside of the local scope of another function