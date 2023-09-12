class Car():
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def carInfo(self):
        print(f"the {self.brand},{self.model} is {self.color}")
        
class Suv(Car):
    def __init__(self,brand,model,color):
        self.car = False
        super().__init__(brand,model,color)
        
    def carInfo(self):
        super().carInfo()
        print("is also a SUV")
        
car1 = Car("Nissan","Kashkai","Blue")
suv2 = Suv("13123","123123","123123")

Suv.carInfo(suv2)



