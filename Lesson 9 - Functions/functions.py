def hello_world():
    print("Hello World")


hello_world()    
print()

# def sum(num1, num2):
#     return num1 + num2

# total = sum(2, 3)
# print(total)
    

def sum(num1=0, num2=0):
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total = sum(5, 2)
print(total)



def multiple_items(*args):
    print(args)
    print(type(args))
    
multiple_items("Mia", "Lohr", "Taylor")




def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
mult_named_items(first = "Mia", last = "Tresenio")    