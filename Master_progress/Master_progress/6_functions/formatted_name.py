# Return values
# A fxn doesn't always have to display output direct. It can be
#  used to process data and return a value or set of values.
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title() # Using the keyword return.
    
musician = get_formatted_name('jimmi', 'hendrix')
print(musician)

# Making an optional argument
# Lets say we want to exapand get_formatted_name() to include
#  middle names. 
def get_formatted_name(first_name, middle_name, last_name): # Add parameter.
    """Return a full name, neatly formatted."""
    full_name = f"\n{first_name} {middle_name} {last_name}" # Add parameter.
    return full_name.title()

musician = get_formatted_name('jimi', 'lee', 'hendrix') # Add argument.
print(musician)

# This only works if there are 3 arguments to pass, what if you only have
#  the first and last name?

def get_formatted_name(first_name, last_name, middle_name=''): # We have to
#  to give the third parameter an empty value. 
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"\n{first_name} {middle_name} {last_name}"
    else:
        full_name = f"\n{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)

musician = get_formatted_name('john', 'booker', 'lee')
print(musician)
