# Nesting 

# You can nest dictionaries inside a list, a list of items inside a dictionary,
# or even dictionaries inside of dictionaries.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2] # Now we have a batallion!

for alien in aliens:
    print(alien)

print()

# A batallion is great, an army is better.

aliens = [] # Start with an empty list 

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# Show the first 5 aliens.
for alien in aliens [:5]:
    print(alien)
print("...")

print(f"The total number of aliens: {len(aliens)}.")

# All 30 objects are the same but we can modify them with a for loop and an
# if statement.

# You can even expand on the loop with an elif block for super powerful aliens.