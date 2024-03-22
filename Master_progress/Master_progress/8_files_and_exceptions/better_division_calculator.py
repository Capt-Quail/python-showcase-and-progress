# Python uses special objects called exceptions to manage errors that arise 
# during a program's execution.
# When you think an error may occure, you can use a try-except block.
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
# You're finding this out way too late, but PEP8 says to use 4 spaces per
# indentation level.   
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break 
    try: 
        answer = float(first_number) / float(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    except ValueError:
        print("Please print a valid number!")
    else:
        print(answer)
