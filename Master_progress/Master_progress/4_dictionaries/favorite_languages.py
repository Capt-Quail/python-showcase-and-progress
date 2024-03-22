# You can also use a dictionary to store one kind of information about many
# objects.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }

# To use this dictionary, given the name of a person who took the poll, 
#you can easily look up their favorite language.
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
print()

favorite_tortures = {
    'garrett': 'the pear of anguish',
    'josh': 'quartering',
    'kacy': 'quartering',
    'melinda': 'the bloody eagle'
    }
for key, value in favorite_tortures.items():
    print(f"{key.title()}'s favorite torture method is {value}.\n")

# But lets say that you wanted to loop through just the keys in a dictionary.
for name in favorite_tortures.keys(): # You use the keys() method!
    print(name.title())

print()

# However, looping through keys is the default behavior when looping
# through dictionaries.

# The code would have worked exactly the same when wrriten as:
    
for name in favorite_tortures:
    print(name.title())

print()

# I don't know how to separate this in the lesson, but learn.

friends = ['garrett', 'melinda'] # We want to send a message a list of
# friends in group.
for name in favorite_tortures.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        tortures = favorite_tortures[name].title()
        print(f"\t{name.title()}, I see you like {tortures}!")

if 'alex' not in favorite_tortures.keys(): #This lets us a send a message to 
    # someone who needs to take our family torture poll
    print("Alex, take our freaking poll!")
print()

# Looping through keys in a particular order
for name in sorted(favorite_tortures.keys()): # Temp sort of the loop of names returned.
    print(f"{name.title()}, thank you for taking the poll.")
print()

# Looping through all the values in a dictionary 
print("The following tortures have been mentioned:")
for tortures in favorite_tortures.values():
    print(tortures.title())
print()

# This approacjh is fine, but what if a lot of other people love the same
# torture?

# For that we have a set() -- when you wrap a set around a collection of
# values that contains duplicate items, Python identifies the unique items in
# the collection and builds a set from those items.
print("The following tortures have been mentioned:")
for tortures in set(favorite_tortures.values()):
    print(tortures.title()) # Tada!
