from pathlib import Path # Pathlib is a library that helps with handling
                         # paths on/from any operating software.

path = Path('pi_digits.txt')
contents = path.read_text()#.rstrip()# A little hard to tell on this IDE but by
                                     # nature read_text() returns an aditional 
                                     # blank line after the last line is 
                                     # called. We strip that space.
 
lines = contents.splitlines() # If you're working with individual lines in a
                              # file, you don't need to strip whitedspace
for line in lines:            # when reading the file. The splitlines() method
    print(line)               # returns a list of all the lines in the file, 
                              # which we assign to the variable lines
