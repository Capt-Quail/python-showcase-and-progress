# Sometimes you know ahead of time how many arguments a function needs to
#  accept. Fortunately, Python allows a function to collect an arbitrary
#  number of arguments from the calling statement.
# For example, consider a fxn that builds a pizza. It needs to accept a number
#  of toppings, but you can't know ahead of time how many toppings a 
#  person will want. The following fxn has only one parameter, *toppings,
#  but this parameter collects as many arguments as the calling line
#  provides. 
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Lets modify the code to create a fxn that describes the pizza. 
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing positional and arbitrary arguments
# If you want a fxn that accepts several different kinds of arguments,
#  the parameter that accepts an arbitrary nymber of arguments must be 
#  placed last in the fxn definition.
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')