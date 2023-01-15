
# Assignment
# Class -03

# 1. Create CRUD (Create, Read, Update, Delete) Operation.

raju_mia_info = ['RAJU', 'MIA', 23, 'DHAKA', 'DIU']
while True:
    user_input = input("Inter what do you want to do: (read/add/update/deleted/close): ")
    if user_input == "close":
        print("Thank You, app is close.")
        break
    elif user_input == "read":
        print("This is Your List: ", raju_mia_info)

    elif user_input == "add":
        add_value = input("Inter your new value: ")
        raju_mia_info.append(add_value)
        print("This is your New list: ", raju_mia_info)

    elif user_input == "update":
        change_value = input("Inter your changes value: ")
        new_update_value = input("Inter Your Update Value: ")
        if change_value in raju_mia_info:
            index_track = raju_mia_info.index(change_value)
            raju_mia_info[index_track] = new_update_value
            print("This is your Update New list: ", raju_mia_info)
        else:
            print("Value is not match! Try again plz")

    elif user_input == "deleted":
        delete_value = input("Inter Your Delete Value: ")
        if delete_value in raju_mia_info:
            raju_mia_info.remove(delete_value)
            print(delete_value, "is delted from the list.")
            print("So, This is Your New List- after Deleted: ", raju_mia_info)
        else:
            print("Your Intered Value Not matched!- plz try Again!")

    else:
        print("Your Input is Invalid-- plz Inter the Currect Input!")



