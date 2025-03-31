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