def addmod(*args):
    return sum(args)

class Car():
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def carInfo(self):
        print(f"the {self.brand},{self.model} is {self.color}")
        
