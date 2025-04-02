accounts = {
    "Alice": {"balance": 1000.0, "history": []},
    "Bob": {"balance": 1500.0, "history": []},
}


def deposit(name, amount):
    accounts[name]["balance"] += amount
    accounts[name]["history"].append(("Deposit", amount))
    print("Deposit successful\n")


def withdraw(name, amount):
    if accounts[name]["balance"] > amount:
        accounts[name]["balance"] -= amount
        accounts[name]["history"].append(("Withdraw", amount))
        print("Withdraw successful\n")
    else:
        print("Insufficient money.\n")


def show_history(name):
    print(f"\nTransaction History for {name}:")
    for transaction in accounts[name]["history"]:
        print(f"{transaction[0]} of ${transaction[1]}")


while True:
    name = input("Enter your name: ")
    if name not in accounts:
        print("User not found!\n")
        break

    operation = float(input("Enter the operation:\n1- Deposit\n2- Withdraw\n3- Show History\n4- Exit\n"))
    if operation == 1:
        amount = float(input("Enter the amount for the deposit: "))
        deposit(name, amount)
    elif operation == 2:
        amount = float(input("Enter the amount for the withdraw: "))
        withdraw(name, amount)
    elif operation == 3:
        show_history(name)
    elif operation == 4:
        break
    else:
        print("Invalid choice. Try again!!")
