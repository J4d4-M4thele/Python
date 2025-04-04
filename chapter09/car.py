class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # setting default value
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back the odometer!")    

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """modelling an electric car battery"""
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size 

    def describe_battery(self):
        """Prints statement describing battery"""
        print(f"This car has a {self.battery_size}-kwh battery.")                       

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
            
        print(f"This car can go about {range} miles on a full charge.")

#creating class instance
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# # modifying attribute values
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# # incrementing attribute's value through a method
# my_used_car = Car('subaru', 'outback', 2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
