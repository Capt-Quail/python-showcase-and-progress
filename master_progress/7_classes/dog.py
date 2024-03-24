# Classes are fundamental to OOP and without them we could not represent real
# world scenarios through data.

# Making an object from a class is called initilization, and you work with
# instances of a class. 

class Dog: # Our object
	"""A simple attempt to model a dog."""
	
	def __init__(self, name, age): # The __init__() method with three
	     # parameters, the first being self wehich gives the instance access to
	     # attributes and methods in a class.
	  	"""Initialize name and age attributes."""
	  	self.name = name
	  	self.age = age 
	  	
	def sit(self):
	    """Simulate a dog sitting in response to a command."""
	  	print(f"{self.name} is now sitting.")
	  	  
	def roll_over(self):
	  	"""Simulate rolling over in response to a command."""
	  	print(f"{self.name} rolled over!")
	  
	def defend(self):
	    """Man's best friend is man's final stand."""
	    print(
             f"{self.name} is priming thermal nuclear warheads.\n"
	           "*warheads primed*\n"
	         f"{self.name} is ready to prove their honor."
	      	 )
	      
	def greet(self):
	    """Simple introduction."""
	    print(
			  f"My dog's name is {self.name} and they are {self.age} years old."
			 )