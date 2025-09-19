def show_balance(balance):
    print(f"Your balance is ${balance:,.2f}")

def deposit():
    amount = float(input("How much do you want to deposit? $"))
    print(f"Amount deposited: ${amount:,.2f}")

    if amount < 0:
        print("That's not a valid amount!")
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient funds")
        return 0 
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0 
    else:
        return amount
 
def exit():
    pass


def main():
    balance = 0
    is_running = True

    while is_running:
        print("================================")
        print("Banking Program")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("================================")

        user_input = input("Enter your choice (1-4): ")

        if user_input == '1':
            show_balance(balance)
        elif user_input == '2':
            balance += deposit()
        elif user_input == '3':
            balance -= withdraw(balance)
        elif user_input == '4':
            is_running = False
        else:
            print("Invalid input")
    print("\nThank you! Have a nice day")

if __name__ == '__main__':
    main()
