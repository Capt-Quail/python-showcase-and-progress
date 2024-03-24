# We'll be working with functions for all of chapter 8. Starting with
#  a super simple little guy named greet_user().

def greet_user(): # Keyword 'def' to define a fxn. Called a fxn definition.
    """Display a simple greeting.""" # This is the 'docstring'. 
    print("Hello!") # This is the only line of code in our simple fxn.

# Passing information to a fxn.
def greet_user(username): # Now when we call the fxn, we're expected to 
#  provide a username
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

# We can improve the functionality of this fxn by adding a while loop. 
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
    
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}!")
# Simnce this loop is infinite we want to both set a quit condition but still 
#  allow the user to quit at any point, for this--we use a break statement.