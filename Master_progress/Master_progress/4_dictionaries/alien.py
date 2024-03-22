alien_0 = {'color': 'green', 'points': 5} # This is a collection of key-value
# pairs.
# Congratulations! You made your first dictionary!
print(alien_0['color'].title())
print(alien_0['points'])
print()

# Now if a player, lets say, shoots down this alien, you can track how many 
# points are earned by wrapping that call in a function.
new_points = alien_0['points']
print(f"You just earned {new_points} points!\n")

# Since dictionaries are dynamic we can add additional data at will!
print(alien_0)
print()

alien_0['x_position'] = 0 # This positions the alien at start/0, the top left
# of the screen. 
alien_0['y_position'] = 25 # This places him 25 pixels from the top of the
# screen.
print(alien_0) # Notice dictionairies keep the order in which they're defined.
print()

# Sometimes its more useful to start with an empty list and then fill it!
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
print()

# Modifying a dictionary is as easy as writing over a new defined key-value
# pair with a dictionary of the same name.
alien_0 = {'color': 'green'}

print(f"The alien is {alien_0['color']}.\n")
alien_0 = {'color': 'yellow'}
print(f"The alien is now {alien_0['color']}.\n") # Bobs ur uncle

# Now our alien has gone from green to yellow! But lets try something more
# complex.

# Lets track the position of an alien that can move at different speeds.

# We'll store a value representing the alien's current speed and use it to
# determine how far to the right the alien should move.
alien_0 = {'x-position': 0, 'y-position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x-position']}")

# Move the alien to the right.
# Determine how far to move the alien based on it's current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien (lol).
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x-position'] = alien_0['x-position'] + x_increment

print(f"New position: {alien_0['x-position']}")
print()
# In summary because this alien was of 'medium' speed, he moved to spaces.

# When you no longer need a piece of information, use the del statement.
alien_0 = {'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0) # Bobs ur uncle.
