# The simplest kind of 'if' statement includes one test and one action:
    # if conditional_test:
        # do something

# You can put any kind of conditional test in the first line and just about any
# action in the indented block following the test.

age = 17
if age >= 18:
    print("You are old enough to vote!") # This test passes and calls to print
    # your statement! Lets add another line
    print("Have you registered to vote?") # Python's 'if-else' syntax allows 
    # for a different choice if conditions aren't met
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote once you turn 18.")
    
