# Consider a list of users who are banned from commenting on a forum. Check
# whether a user has been banned before allowing that person to submmit a 
# comment. 
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")