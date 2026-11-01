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
        self.brightness = brightness #0-100

    def display_info(self):
        print(f"""
Name: {self.name}
Status: {self.status}
Mode: {self.mode}
Brightness: {self.brightness}%
""")
        
    def update_settings(self, setting_index):
        if setting_index == 1:
            self.name = input("New name: ").title()
        elif setting_index == 2:
            self.status = "ON" if self.status == "OFF" else "OFF"
        elif setting_index == 3:
            self.mode = "COOL" if self.mode == "WARM" else "WARM"
        elif setting_index == 4:
            self.brightness = get_int("Change brightness to: ")
            while self.brightness < 0 or self.brightness > 100:
                print("Brightness must be between the 0-100 range")
                self.brightness = get_int("Change brightness to: ")
        else:
            print("Setting not available")

def save_data(rooms, filename="smart_light.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(rooms, f)

def load_data(filename="smart_light.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def linear_search(arr, target):
    for x in range(len(arr)):
        if arr[x].name.lower() == target.lower():
            return x
    return -1

rooms = load_data() #array containing classes (settings) of each room
n = len(rooms)
while True:
    print("")
    print("=====MENU=====")
    for x in range(n): #prints names of current rooms
        print(f"{x+1}. {rooms[x].name}")
    print(f"""{n+1}. Add room
{n+2}. Remove room
{n+3}. Exit""")
    room_choice = get_int("Choice: ")
    if room_choice >= 1 and room_choice <= n + 3: #if in the range of 1st room until remove room options
        if room_choice <= n+1: #if room_choice is a room and not adding/removing from array
            print("=====CURRENT SETTINGS=====")
            rooms[room_choice-1].display_info() #outputs settings of the lights in that room
            print(f"""1. Change room name
2. Turn {"OFF" if rooms[room_choice-1].status == "ON" else "ON"}
3. Change light mode to {"WARM" if rooms[room_choice-1].mode == "COOL" else "COOL"}
4. Adjust brightness
5. Cancel""")
            setting_choice = get_int("Setting: ")
            if setting_choice == 5:
                pass
            else:
                rooms[room_choice-1].update_settings(setting_choice)
                save_data(rooms)
        elif room_choice == n+1: #if room_choice = add room
            if n < 5: #max room number == 5
                new_name = input("Name of new room: ")
                rooms.append(Settings(new_name.title(), "ON", "COOL", 100)) #adds new room with default settings on, cool and 100% brightness
                save_data(rooms)
                n += 1
            else:
                print("You have reached the max number of rooms. Please remove a room first.")
        elif room_choice == n+2: #if room_choice = remove room
            if rooms:
                target = input("Enter room name to remove: ")
                index = linear_search(rooms, target)
                if index != -1:
                    choice = input("Are you sure? (Y/N): ").upper()
                    while choice not in ("Y", "N"):
                        print("Invalid input. Please choose 'Y' or 'N'")
                        choice = input("Are you sure? (Y/N): ").upper()
                    if choice == "Y":
                        del rooms[index]
                        save_data(rooms)
                        n -= 1
                    else:
                        print("Action cancelled")
                else:
                    print("Room not found")
            else:
                print("There are currently no rooms. Please add a room first.")
        elif room_choice == n+3: #if room_choice = exit
            break
    else:
        print("Invalid option. Please choose between 1-" + str(n+3))