class Car:
    def __init__(self, brand, model):
        self._brand = brand  # Protected attribute
        self.__model = model  # Private attribute

    def start(self):
        # Method to start the car
        print(f"{self.__model} is starting.")

    def get_brand(self):
        # Getter method to access the protected attribute
        return self._brand

    def set_brand(self, new_brand):
        # Setter method to modify the protected attribute
        self._brand = new_brand


