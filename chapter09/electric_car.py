from car import *

class ElectricCar(Car):
    """Represent aspects of a car - specifically electric"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # defining child class attributes
        # self.battery_size = 40

        # accessing Battery class
        self.battery = Battery()

    def fill_gas_tank():
        print("This car doesn't have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())  
my_leaf.battery.describe_battery()      
my_leaf.battery.get_range()
