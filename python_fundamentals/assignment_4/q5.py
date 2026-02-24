class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
class Car(Vehicle):
    def __init__(self,brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats
        
class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

car1 = Car("bmw", "m5", 5)
print(car1.brand)
bike1 = Bike("pulsar", "ns125", 125)
print(bike1.model)