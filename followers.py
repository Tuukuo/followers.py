
users_list = {}

def followers_system(user_name,list):
    users_list[user_name] = list

followers_system("User1",["dorcas","mikisa","nancy","mwanasha"])
followers_system("User2",["latifa","loice","susan"])
print(users_list)

def search(id):
    list_of_users = users_list.keys()
    if id in list_of_users:
        print(users_list[id])
    
search("User2")









