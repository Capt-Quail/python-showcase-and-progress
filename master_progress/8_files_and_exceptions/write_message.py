from pathlib import Path

# Writing multiple lines to a program.
contents = "I love programming.\n"
contents += "I also love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents) # The write_text() method lets you write
# to a file you create. 