# Writing clear prompts.
# Any time you use the input() function, you should include a clear,
# easy-to-follow prompt that tells the user exactly what kind of information
# you're looking for.
# Sometimes you'll want to write a prompt that's longer than one line.
# You can assign your prompt to a variable and pass that variable to the
# input() function. This allows you to build your prompt over several lines,
# then write a clean input() statement. 
prompt = "If you share your name, we can personalize the messages you see.\n"
prompt += "\nMay you burn in the depths of hell for all eternity.\n"
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"Hello, {name}!")