inventory = {
    "Laptop": 5,
    "Mouse": 10,
    "Keyboard": 8,
    "Headphones": 3,
}

while True:
    item_name = input("Enter the name of the item, for exit press 0: ")
    if item_name == "0":
        print("Exiting...")
        break
    quantity = int(input("Enter the quantity: "))

    item_found = False

    for item in inventory:
        if item_name == item:
            item_found = True
            if inventory[item] >= quantity:
                inventory[item] -= quantity
                print(f"Order confirmed: {quantity} {item}\n")
            else:
                print("Rejected due to insufficient stock.\n")
            break
    if not item_found:
        print("Item not found in inventory.\n")