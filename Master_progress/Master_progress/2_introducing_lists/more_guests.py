# You just found a bigger dinner table, so now more is available. Think
# of three more guest to invite to dinner.
# Start with your progam from exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
guest_list = []

guest_list.append('marty smith')
guest_list.append('brenda smith')
guest_list.append('bill smith')
guest_list.append('garrett smith')
guest_list.append('melinda smith')
guest_list.append('rodney smith')
guest_list.append('lisa smith')
guest_list.append('alex smith')
guest_list.append('kacy mcmillan')
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

print(
    "Wonderful news, undead Team, we've found a larger space and are expanding"
    " the guest list an adequate degree. \n"
    )

guest_list.insert(1, 'abraham lincoln')
guest_list.insert(5, 'alexander hamilton')
guest_list.append('dalinar kholin')

for guest in guest_list:
    print(
        "Dear valued friend, emissary of hope, and bastion of history, "
        f"{guest.title()}, \n \nToday we spit in the face of death at the "
        "greatest eatery of all--Sweet Tomatoes of University Drive in Coral "
        "Springs on May 28th at 6PM. \nMay your apetite be as large as your "
        "impact on the world. \nYours Truly, \nJoshua smith \n"   
    )
