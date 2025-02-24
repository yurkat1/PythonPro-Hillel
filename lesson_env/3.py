import random

class Car:
    def __init__(self, trip_distance, model, color, fuel = random.randrange(0, 9)):
        self.fuel = fuel
        self.trip_distance = trip_distance
        self.model = model
        self.color = color

    def move(self, distance):
        self.distance = distance

    # @property
    # def trip_distance(self):
    #     return self.trip_distance
    #
    # @trip_distance.setter
    # def trip_distance(self, move(random.randrange(0, 9))):
    def start_race(self):
        race_dist = 5000  #место назначения гонки
        desired_dist =  #желаемый пункт назначения


    def show_info(self):
        return f"Fuel - {self.fuel}, Trip_distance - {self.trip_distance}, model - {self.model}, color - {self.color}"
#
# while race_dist < desired_dist:
#     move(distance = random.randrange(0, 9))


car1 = Car("3300", "BMW", "Black")
print(car1.show_info())
car2 = Car("2900", "Toyota", "Blue")
print(car2.show_info())
car3 = Car("3500", "Ferrari", "Red")
print(car3.show_info())
#

