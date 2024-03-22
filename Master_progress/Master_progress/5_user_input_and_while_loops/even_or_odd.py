# The modulo operator.
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0: # Even numbers are always divisible by two
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")