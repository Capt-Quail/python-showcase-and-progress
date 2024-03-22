"""A Class that can be used to represent a car.""" # This is a module-level 
                                                   # docstring.

# Working with Classes and Instances
# Start with writing the Car class as any other.
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year): #Attributes can be defined without 
    # being passed in as parameters. These attributes are defined in the
    # __init__ mehtod, where they're asigned a default value.
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Setting it to zero as a default or optional
        # value. 
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title() # This method requires us to store a value in
        # in a variable and return it so that it can be further maniputlated by
        # methods and functions 
        
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage): # Do NOT forget to add your additional 
    # parameter here.
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
        self.odomoter += miles        
# We can even add an attritubute that changes over time, for example, the 
# odometer reading. 
# -----
# You can modify an attributes value in three ways:
# - Change the value directly through an instance
# - Set the value through a method
# - Or increment the value through a method
# -----
# The simplest way to modify the value of an attribute is to access the 
# attribute directly through an instance, for example, setting the odometer
# reading to 23.
# -----
# Sometimes this method may be useful, but other times you may want to write a 
# method that does this for you, for example, update_odometer().
# -----
# You can even extend the usefulness of a simple method with the addition
# of a little logic! 