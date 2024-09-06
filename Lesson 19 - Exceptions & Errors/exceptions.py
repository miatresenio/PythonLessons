class JustNotCooError(Exception):
    pass

x = 2
try:
    raise JustNotCooError("This just isn't cool, man.")
    # raise Exception("I'm a custom exception!")
    # # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.") 
except NameError:
    print('NameError means something is probably undefined.')    
except ZeroDivisionError:
    print('Please do not divide by zero.') 
except Exception as error:
    print(error)       
else:
    print('No errors!')  
finally:
    print("I'm going to print with or without an error.")  
        