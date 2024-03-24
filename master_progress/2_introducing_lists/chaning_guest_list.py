# You just lesarned that one of your guests can't make the dinner, so
# you need to send out a new set of invitations. You'll have to think of 
# someone else to invite.
# Start with your program from exercise 3-4. Add a print () call at the end of
# your program, stating the name of the guest who can't make it.
# Modify your list, replacing the name of the guest who can't make it with the
# name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still
#in your list.
guest_list = []

guest_list.append('marty smith')
guest_list.append('brenda smith')
guest_list.append('bill smith')
guest_list.append('garrett smith')
guest_list.append('melinda smith')
guest_list.append('rodney smith')
guest_list.append('lisa smith')
guest_list.append('alex smith')
guest_list.append('kacy smith')
guest_list.append('anne frank')
guest_list.append('nikola tesla')
guest_list.append('attila')

removed_guest = 'anne frank'
guest_list.remove(removed_guest)
guest_list.insert(9, 'queen elizabeth of england')
print(f"{removed_guest.title()} unfortunately cannot make it. \n")

for guest in guest_list:
    print(
        f"{guest.title()}, \nYou are formally invited to Joshua's"
        " 'Post-life Full-life Beyond the Grave Extravaganza', with a revised "
        "time of on May 28th at your mom's house. \nBring salad and beer. \n"
    )
