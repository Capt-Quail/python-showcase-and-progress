# If you could invite anyone, living or dead, to dinner, who would you invite?
# Make a list that includes at least three people you'd like to invite to 
# dinner. Then use your list to print a message to each person, inviting them
# to dinner.
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

for guest in guest_list:
    print(
        f"{guest.title()}, \nYou are formally invited to Joshua's"
        " 'Post-life Full-life Beyond the Grave Extravaganza', with a revised "
        "time of on May 28th at your mom's house. \nBring salad and beer. \n"
    )