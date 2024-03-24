# Use a variable to represent a person's name, and include some whitespace
# characters at the begining and the end of the name. Make sure you use each
# character combination, "\t" and "\n," at least once.
# Print the name once, so the whitespace around the name is displayed. 
# Then pring the name using each of the three strip functions.
bigbros = []

bigbros.append("\tgarret smith  \n")
for bigbro in bigbros:
    print(bigbro)
    print(bigbro.title().lstrip())
    print(bigbro.title().rstrip())
    print(bigbro.title().strip())
