# The 'break' statement lets you exit a while loop immediately without running
# additional code and regardless of conditional tests.
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True: # A loop that starts withj 'while True' will loop endlessly until 
    #a break statement.
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")