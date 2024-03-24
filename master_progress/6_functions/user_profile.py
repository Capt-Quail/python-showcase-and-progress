# Sometimes you'll want to accept an arbirtrary number of arguments, but you
#  won't know ahead of time want kind of information will ne be passed to the 
# fxn. In this case, we can write functions that accept as many key-value pairs
# as the calling statement provides.
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info
	
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)