# The following was an at the time very complex example that culminated to a
# a not so complex program demonstrating the capabilities of lists.
available_toppings = ['mushroom', 'olives', 'green_peppers',
                      'pepperoni', 'pineapple', 'extra_cheese']

requested_toppings = ['mushrooms', 'french_fries', 'extra_cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\n Finished making your pizza!")