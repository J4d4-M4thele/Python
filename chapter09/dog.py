# class declaration
class Dog:
    """A simple dog model"""
    def __init__(self, name, age):
        """initialise name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate dog sitting in response to command"""
        print(f"{self.name} is now sitting.")

    def roll_over (self):
        """Simulate dog rolling over in response to command"""
        print(f"{self.name} rolled over!")  

# creating an instance of the class
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

# accessing attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# calling methods
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()