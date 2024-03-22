# This is an example of a 'positional argument' to pass more than one argument.
def describe_pet(animal_type, name): # You must pass an argument in order of 
#  your parameters.
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {name.title()}.")

# You can use multiple fxn calls too! Asd many times as needed. 
describe_pet('hamster', 'momma hamster')
describe_pet('ocelot', 'feebie')

# 'Keyword arguments' free you from needing to worry about correctly
#  ordering your arguments.
def describe_pet(animal_type, name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {name.title()}.")

describe_pet(animal_type='tiger', name='jerry')
describe_pet(name='terry', animal_type='liger')

# Default values
# If you notice a large number of similarities across calls, you can simplify
#  your code by ascribing default values to paramters.

# Let's assume we've gotten a lot of calls that describe dogs for describe_pet.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')