# How the input() function works.
# The following program asks the user to enter some text, then displays that 
# message back to the user.
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
# The pprogram waits while the user enters their response and continues after
# the user presses ENTER. The response is assigned to the variable message,
# then print(message) displays the input nack to the user. 
# We can make the parrot program run as long as the user wants by putting most
# of the prgram inside a while loop.
# We'll define a 'quit value' to keep the program running as long as the user
# has not entered the value.
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit': # This nifty addition prevents printing 'quit'
        # while exiting!
        print(message)

# Using a flag to control multiple conditions 
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True 
while active:
    message = input(prompt)
    
    if message == 'quit': # Now we can addition elif statements to determine
        # alternate events to cause False
        active = False 
    else:
        print(message) 