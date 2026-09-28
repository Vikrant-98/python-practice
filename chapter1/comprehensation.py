menu = ["chai", "milk", "sugar", "ginger", "cardamom", "cinnamon"]

list_tea = [item for item in menu if len(item) > 4]

print(f"Items in the menu with more than 4 characters: {list_tea}")