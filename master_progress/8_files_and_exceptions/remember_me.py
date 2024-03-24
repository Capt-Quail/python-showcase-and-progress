# Saving user-generated data
from pathlib import Path
import json

def get_sorted_username(path):
    """Get sorted username if available."""
    if path.exists():
       contents = path.read_text()
       username = json.loads(contents)
       return username 
    else:
       return None # a function should either return the value you're expecting
       # or None.

def get_new_username(path):
    """Prompt for a new username"""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username 

def greet_user():
    """Greet user by name."""
    path = Path('username.json')
    username = get_sorted_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")