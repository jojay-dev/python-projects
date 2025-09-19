def show_balance(balance):
    print(f"Balance: ${balance:,.2f}")

def deposit():
    try:
        amount = float(input("Deposit $"))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return 0
    if amount < 0:
        print("Invalid amount!")
        return 0
    else:
        print(f"Deposited: ${amount:,.2f}")
        return amount

def withdraw(balance):
    try:
        amount = float(input("Withdraw: $"))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return 0
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        print(f"Withdrew: ${amount:,.2f}")
        return amount

def quit_program():    
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
