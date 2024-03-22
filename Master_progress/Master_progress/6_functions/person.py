# Returning a definition.
def build_person(first_name, last_name, age=None): 
    """Return a dictionary of information about a person.""" # Docstring.
    person = {'first': first_name, 'last': last_name} # Build the dictionary.
    if age:
        person['age'] = age 
    return person # Return the values in the dictionary.

musician = build_person('jimi', 'hendrix')
print(musician)

# You can even easilly add a third optional parameter!
musician = build_person('jimi', 'hendrix', age=27)
print(musician)