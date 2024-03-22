# How can we use an 'if' statement to determine a person's admission rate? 
# By using if-elif-else syntax.
age = 12

if age < 4:
    print("Your admissions cost is $0.")
elif age < 18:
    print("Your admissions cost is $25.")
else:
    print("Your admissions cost is $40.")
# We can refactor this chain since it is more concise to set the price inside 
# the if-elif-else chain and have a single print() call that runs after the 
# chain has been evaluated.
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admissions cost is ${price}.")
# You can have as many elif blocks as you want! For instance, if there was a 
# senior discount.
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admissions cost is ${price}.")
# The 'else' statement is not necessary in an if-elif chain. It serves as a 
# catch all, but you can write code where each condition must pass or fail.
age = 66

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age > 65:
    price = 20

print(f"Your admissions cost is ${price}.")