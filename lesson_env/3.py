import random

class Car:
    def __init__(self, trip_distance, model, color, fuel = random.randrange(0, 9)):
        self.fuel = random.randrange(0, 9)
        self.trip_distance = 0
        self.model = model
        self.color = color

    def move(self, distance):
        self.trip_distance += distance  # додаємо відстань до пробігу
        self.fuel -= distance


    def show_info(self):
        return f"Fuel - {self.fuel}, Trip_distance - {self.trip_distance}, model - {self.model}, color - {self.color}"


car1 = Car("3300", "BMW", "Black")
print(car1.show_info())
car2 = Car("2900", "Toyota", "Blue")
print(car2.show_info())
car3 = Car("3500", "Ferrari", "Red")
print(car3.show_info())
#

