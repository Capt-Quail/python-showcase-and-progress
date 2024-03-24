# Using a while loop with lists and disctionaries.
# Filling a dictionary with user input.
# Lets make a polling program in which each pass
#  through the loop prompts for the participant's
#  name and response. We'll use a dictionary because
#  we want to connect each response to a user.

# Start with an emtpy dictionary.
responses = {}
# Set a flag to indicate that poling is active.
polling_active = True
while polling_active:
    # Prompt for the persons name and response.
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb some day? ")
    
    # Store responses in the dictionary.
    responses[name] = response 
    
    #Find out if anyone else is going to take the poll.
    repeat = input("\nWould you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results.
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
