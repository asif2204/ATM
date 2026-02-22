# ATM Simulation Project

balance = 0
pin = None

def create_pin():
    global pin
    pin = input("Create your 4-digit PIN: ")
    if len(pin) == 4 and pin.isdigit():
        print("PIN created successfully!")
    else:
        print("Invalid PIN! Try again.")
        create_pin()

def login():
    entered_pin = input("Enter your PIN: ")
    if entered_pin == pin:
        print("Login successful!")
        return True
    else:
        print("Wrong PIN!")
        return False

def check_balance():
    print(f"Your balance is: Rs.{balance}")

def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    balance += amount
    print("Deposit successful!")

def withdraw():
    global balance
    amount = int(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print("Please collect your cash.")
    else:
        print("Insufficient balance!")

# Main Program
print("=== Welcome to ATM ===")

create_pin()

while True:
    if login():
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter choice (1-4): ")

            if choice == "1":
                check_balance()
            elif choice == "2":
                deposit()
            elif choice == "3":
                withdraw()
            elif choice == "4":
                print("Thank you for using ATM!")
                exit()
            else:
                print("Invalid choice!")
