import pickle

def get_int(prompt): #keeps asking until user enters a valid int
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")

class Settings:
    def __init__(self, name, status, mode, brightness):
        self.name = name
        self.status = status #ON/OFF
        self.mode = mode #COOL/WARM
        self.brightness = brightness #1-100

    def display_info(self):
        print(f"""Name: {self.name}
Status: {self.status}
Mode: {self.mode}
Brightness: {self.brightness}%
""")
        
    def update_settings(self, setting_index, rooms):
        if setting_index == 1:
            new_name = input("New name: ").strip().title()
            while not new_name:
                print("Name can't be empty.")
                new_name = input("New name: ").strip().title()
            index = linear_search(rooms, new_name)
            if index != -1: # if name already used by different room
                print("A room with that name already exists.")
                return False #nothing changed
            self.name = new_name
        elif setting_index == 2:
            self.status = "ON" if self.status == "OFF" else "OFF"
        elif setting_index == 3:
            if self.status == "OFF":
                print("The light is off. Turn it on first.")
                return False
            self.mode = "COOL" if self.mode == "WARM" else "WARM"
        else:
            if self.status == "OFF":
                print("The light is off. Turn it on first.")
                return False
            value = get_int("Change brightness to: ")
            while not 0 < value <= 100:
                print("Brightness must be between 1 and 100.")
                value = get_int("Change brightness to: ")
            self.brightness = value
        return True #a setting was changed

def save_data(rooms, account, filename="smart_light.pkl"):
    data = {"account": account, "rooms": rooms}
    with open(filename, "wb") as f:
        pickle.dump(data, f)

def load_data(filename="smart_light.pkl"):
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
        return data["account"], data["rooms"]
    except FileNotFoundError:
        return {}, [] 

def linear_search(arr, target):
    for x in range(len(arr)):
        if arr[x].name.lower() == target.lower(): #if found return room index
            return x
    return -1 #if not found

def main(rooms, account):
    global n
    while True:
        print("")
        print("""=====MENU=====
    1. View rooms
    2. Add room
    3. Remove room
    4. Exit""")
        menu = get_int("Menu: ")

        if menu == 1: #view rooms
            if rooms:
                print("")
                print("=====ROOM MENU=====")
                for x in range(n): #prints names of current rooms
                    print(f"{x+1}. {rooms[x].name}")
                print(f"{n+1}. Back")
                room_choice = get_int("Choice: ")
                while not 1 <= room_choice <= n + 1:
                    print(f"Invalid input. Please choose between 1-{n+1}.")
                    room_choice = get_int("Choice: ")
                if room_choice == n + 1: #Back
                    continue
                print("")
                print("=====CURRENT SETTINGS=====")
                rooms[room_choice-1].display_info() #outputs settings of the lights in that room
                print(f"""1. Change room name
2. Turn {"OFF" if rooms[room_choice-1].status == "ON" else "ON"}
3. Change light mode to {"WARM" if rooms[room_choice-1].mode == "COOL" else "COOL"}
4. Adjust brightness
5. Back""")
                setting_choice = get_int("Change setting (1-5): ")
                while setting_choice < 1 or setting_choice > 5:
                    print("Invalid input. Please choose number between 1-5.")
                    setting_choice = get_int("Change setting (1-5): ")
                if setting_choice == 5:
                    pass
                elif rooms[room_choice-1].update_settings(setting_choice, rooms):
                    print(f"Settings for {rooms[room_choice-1].name.lower()} has been updated.")
                    save_data(rooms, account)
            else:
                print("There are no rooms. Please add a room first.")

        elif menu == 2: #add room
            if n < 5: #max room number == 5
                while True:
                    new_name = input("New room: ").strip().title()
                    if not new_name:
                        print("Name can't be empty.")
                    elif linear_search(rooms, new_name) != -1: #room names must be unique
                        print("A room with that name already exists.")
                    else:
                        break
                rooms.append(Settings(new_name, "ON", "COOL", 100)) #adds new room with default settings on, cool and 100% brightness
                print(new_name, "has been added with default settings.")
                save_data(rooms, account)
                n += 1
            else:
                print("You have reached the max number of rooms. Please remove a room first.")

        elif menu == 3: #remove room
            if rooms:
                target = input("Enter room name to remove: ").strip()
                index = linear_search(rooms, target)
                if index != -1:
                    choice = input("Are you sure? (Y/N): ").upper()
                    while choice not in ("Y", "N"):
                        print("Invalid input. Please choose 'Y' or 'N'.")
                        choice = input("Are you sure? (Y/N): ").upper()
                    if choice == "Y":
                        print(rooms[index].name, "has been deleted.")
                        del rooms[index]
                        save_data(rooms, account)
                        n -= 1
                    else:
                        print("Action cancelled.")
                else:
                    print("Room not found.")
            else:
                print("There are currently no rooms. Please add a room first.")

        elif menu == 4: #exit
            logout_user = input("Logout? (Y/N): ").strip().upper()
            while logout_user not in ("Y", "N"):
                print("Invalid input")
                logout_user = input("Logout? (Y/N): ").strip().upper()
            if logout_user == "Y":
                account["logout"] = True
                save_data(rooms, account)
            break
            
        else:
            print("Invalid option. Please choose between 1-4")

account, rooms = load_data() #load account dictionary, rooms list
n = len(rooms)

if not account: #prompts user to make account
    username = input("Username: ").strip()
    while not username:
        print("Username can't be empty.")
        username = input("Username: ").strip()
    while True:
        password = input("Password: ")
        if not password:
            print("Password can't be empty.")
            continue
        passwordauth = input("Verify password: ")
        if password == passwordauth:
            break
        print("Passwords don't match.")
    account = {"username": username, "password": password, "logout": False}
    save_data(rooms, account=account)
    correct = True
    print(f"Welcome, {username}!")

elif account.get("logout") == True: #if user already has an account and logged out
    username = account.get("username")
    password = account.get("password")
    passwordauth = input("Input password: ")
    countauth = 0
    correct = False
    while passwordauth != password and countauth < 2: #3 tries for password auth
        print("Incorrect password. Try again.")
        passwordauth = input("Input password: ")
        countauth += 1
    if passwordauth == password:
        correct = True
        account["logout"] = False
        save_data(rooms, account)
        print(f"Welcome back, {username}!")

else: #if user is not logged out
    correct = True

if correct:
    main(rooms, account)
else:
    print("Too many incorrect attempts. Access denied.")
