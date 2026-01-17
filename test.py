class Car:
    
    def __init__(self,engine,colour,model,brand,petrol):
        self.engine = engine
        self.colour = colour
        self.model = model
        self.brand = brand
        self.petrol = petrol

    def move(self,instruction):
        if instruction.lower() == "up" or instruction.lower() == "down" or instruction.lower() == "left" or instruction.lower() == "right":
            if car.petrol >= 5:
                print("Enough Petrol")
            else:
                print("Insufficient amount of petrol")
        else:
            print("Invalid instruction input")


car = Car(3.0,"blue",2012,"BMW",2)
print(car.model)
instruction = input("Enter instruction (up,down,left,right): ")
car.move(instruction)