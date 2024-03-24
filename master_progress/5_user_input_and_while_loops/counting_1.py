# Using continue in a loop.
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # Lets us continue our code without breaking out of a loop 
    # without executing the rest of the code.
    
    print(current_number)

# Avoiding infinite loops.
x = 1
while x <= 5:
    print(x)
    x += 1 # Omitting this makes the code run forever becuse it will always be
    # less than 5!
