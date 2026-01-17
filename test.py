class Car:
    
    def __init__(self,engine,colour,model,brand):
        self.engine = engine
        self.colour = colour
        self.model = model
        self.brand = brand


car = Car(3.0,"blue",2012,"BMW")
print(car.model)