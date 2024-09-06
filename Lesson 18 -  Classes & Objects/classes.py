# CLASSES - Blue print for creating objects

class Vehicle:
    def __init__(self,make, model):
        self.make = make
        self.model = model
        
    def moves(self):
        print('Moves along..')
        
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")
        
my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()        

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()


# INHERITANCE - When we have other classes that can inherit from a parent class
class Airplane(Vehicle):
    def __init__(self,make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
   
   
    def moves(self):
        print('Flies along..')
        
class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..') 
        
class Motor(Vehicle):
    pass


cessna = Airplane('Cessna', 'Skyhawk', 'n-12345')            
mack = Truck('Mack', 'Pinnacle')            
yamaha = Airplane('Yamaha', 'Kawasaki')   

cessna.get_make_model()         
cessna.moves()
mack.get_make_model()         
mack.moves()
yamaha.get_make_model()         
yamaha.moves()

print('\n\n')


################################################ 
# POLYMORPHISM - is the ability to behave differently in response to the same input messages.

for v in (my_car, your_car, cessna, mack, yamaha):
    v.get_make_model()
    v.moves()


