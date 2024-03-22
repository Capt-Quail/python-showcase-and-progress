"""A set of classes that can be used to represent electric cars."""

# When you write a child class, the parent class must be part of the current 
# file and must appear before the child class in the file.

from car import Car
 
class ElectricCar(Car): # The name of the parent class must be included 
                        # in parentheses in the definition of a child class.
    """Represent aspects of a car, specific to electric vehicles."""
       
    def __init__(self, make, model, year): # The __init__method takes in the 
                                           # information required to make an
                                           # instance.
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an alectric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery() # We add a new attribute for the battery class.

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery's attributes."""
        print(f"This car has a {self.battery_size}-kwh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
           range = 150
        elif self.battery_size == 65:
           range = 225
           
        print(f"This car can go about {range} miles on a full charge.")