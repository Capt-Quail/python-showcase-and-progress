# Using a while loop with lists and dictionaries 
# Removing all instances of specific values from
#  a list.

# Say you have a list of pets with the value 'cat'
#  repeated several times. To remove all instances
#  of that value, you can run a while loop using
#  the remove() function! (ref. ch 3)

# Start with a list of pets.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat') # Loop the removal of 'cat'

print(pets)
