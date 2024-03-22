# A dictionary in a dictionary.
# When you have several users on a website, each with a unique username, 
# you can use the usernames as the keys in a dictionary.
# Then, you can store information about each user by using a dictionary as the
# value associated with their username.
# The following example will store 3 pieces of information about each user:
users = {
    'aenstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
        
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location' : 'paris',
        },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = (f"{user_info['first']} {user_info['last']}")
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")