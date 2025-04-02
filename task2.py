accounts = {
 "Alice": {"balance": 1000},
 "Bob": {"balance": 250},
 "Charlie": {"balance": 80},
}


def withdraw(name, amount):
    if accounts[name]["balance"] > amount:
        if amount % 10 == 0:
            accounts[name]["balance"] -= amount
            print("Withdraw successful\n")
            return True
        else:
            print("Be sure that amount of withdraw is a multiple of 10\n")
            return False
    else:
        print("Insufficient money\n")
        return False


while True:
    name = input("Enter your name, for exit press 0: ")
    if name == "0":
        print("Exiting...")
        break
    else:
        if name not in accounts:
            print("User not found!\n")
            break
        else:
            amount = float(input("Enter the withdraw amount: "))
            withdraw(name, amount)
