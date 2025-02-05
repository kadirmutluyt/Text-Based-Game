class Room:
    def __init__(self, name, description=None, north=None, east=None, south=None, west=None, item=None):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.item = item
        self.items = []

    def item_add(self, item):
        self.items.append(item)


    def __str__(self):
        return f"{self.name}"


class Player:
    def __init__(self, entrance_room):
        self.current_room = entrance_room
        self.inventory = []
        self.player = Player


    def move(self, direction):
        if direction == "north" and self.current_room.north:
            self.current_room = map_rooms[self.current_room.north]
            print(self.current_room.description)

        elif direction == "east" and self.current_room.east:
            self.current_room = map_rooms[self.current_room.east]
            print(self.current_room.description)

        elif direction == "south" and self.current_room.south:
            self.current_room = map_rooms[self.current_room.south]
            print(self.current_room.description)

        elif direction == "west" and self.current_room.west:
            self.current_room = map_rooms[self.current_room.west]
            print(self.current_room.description)
        else:
            print("You can't go this way! ")



    def take(self, item):
        # if item == "key" and not self.inventory == "knife":     # önemli yer!
        #     print("You need something sharp to open it! ")
        #     return  #   !
        # elif item in self.current_room.items:           # if ?
        #     self.inventory.append(item)
        #     print(f"{item} added to inventory.")
        # else:
        #     print("There is no such item in this room.")
        if item == "key" and item in self.current_room.items and self.inventory == "knife":  # Eğer item odada varsa
            self.inventory.append(item)
            self.current_room.items.remove(item)  # Anahtarı aldıktan sonra odadan kaldır.
            print(f"{item} added to inventory.")
        if item == "knife" and item in self.current_room.items:           # elif
             self.inventory.append(item)
             self.current_room.items.remove(item)  # Bıçağı aldıktan sonra odadan kaldır.
             print(f"{item} added to inventory.")
        else:
            print("There is no such item in this room.")

    def use(self,item):
        if item in self.inventory:
            if self.current_room.name == "closet" and item == "knife":
                print("You use the knife to open the closet and there is a key.")
                self.current_room.items.append("key")
            else:
                print("You can't use this item here.")
        else:
            print("You don't have that item in your inventory.")

        if item in self.inventory:
            if self.current_room.name == "exit" and item == "key":
                print("You exit the home. You are free now!")
                print("Game Over!")
                return

            else:
                print("You can't use this item here.")
        else:
            print("You don't have that item in your inventory.")
    def drop(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You drop {item}. ")
        else:
            print("You don't have that item in your inventory.")

    def show_inventory(self):
        if self.inventory:
            print("Items in your inventory: ")
            for item in self.inventory:
                print("-", item)
        else:
            print("Your inventory is empty.")



def main():
    # Items
    knife = "knife"
    key = "key"


    # Rooms and others
    entrance_room = Room("entrance", "An entrance room.There is a door in the south.", None, None, "kitchen", None, None)
    kitchen = Room("kitchen", "\nYou are in the kitchen.There is a sharp knife on the table.","entrance", "living room", None, None,"knife")
    living_room = Room("living room","\nYou are in the living room.","closet", None, "exit", "kitchen",None)
    closet = Room("closet","\nThere is a closed closet.Maybe you can open it with something sharp.",None,None,"exit","kitchen","key")
    exit = Room("exit", "\nThere is a room but its locked.", "closet", None, None, "living room",None)



    global map_rooms
    map_rooms = {
        entrance_room.name: entrance_room,
        kitchen.name: kitchen,
        living_room.name: living_room,
        exit.name: exit,
        closet.name: closet,
    }

    kitchen.item_add(knife)
    closet.item_add(key)

    # Player
    player = Player(entrance_room)

    # Start
    print("\nWelcome to basic text game for beginners!\nI hope you are ready!\nGame Starting!\n")
    #print(player.current_room)
    print(player.current_room.description)

    # PLayer Commands
    while True:
        command = input("What do you want to do? (go/take/drop/use/inventory/quit) ").strip().lower()

        if command == "quit":
            print("You are quitting the game D: ")
            break
        elif command == "go":
            direction = input("which direction do you want to go? (north/east/south/west) ").strip().lower()
            player.move(direction)
        elif command == "take":
            item = input("Type the name of the item you want to take: ").strip().lower()
            player.take(item)
        elif command == "drop":
            item = input("Type the name of the item you want to drop: ").strip().lower()
            player.drop(item)
        elif command == "use":
            item = input("Type the name of the item you want to use: ").strip().lower()
            player.use(item)
        elif command == "inventory":
            player.show_inventory()
        else:
            print("Invalid command.Try this commands 'go', 'use' , 'take' , 'drop' , 'inventory' or 'quit'.")


main()

