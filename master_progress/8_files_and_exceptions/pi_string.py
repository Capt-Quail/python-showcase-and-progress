from pathlib import Path 

path = Path('pi_million_digits.txt')
# We read the data from the file we want to use with the read_text() method and
# assign it to a variable 
contents = path.read_text()

lines = contents.splitlines()
# Empty variable to store the written data
pi_string = ''
for line in lines:            
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))