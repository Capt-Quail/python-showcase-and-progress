from pathlib import Path

# wrapping our code in a function called count_words
def count_words(path):
    """Count the apporximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass # Wow, we're choosing to do nothing here, we can come back later.
    else:
        # Count the approximate number of words in a file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
        'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)