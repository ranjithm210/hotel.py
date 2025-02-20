import datetime

# Initialize variables
exit_program = False
inserted = False
balance = 20000
actual_pin = None
blocked = False
attempt = 0
transactions = []

while True:
    print("\nWelcome to SBI ATM")
    print("Please insert your ATM card.")

    if not inserted:
        x = int(input("Press 1 to CONTINUE, 2 to EXIT: "))
        
        if x == 1:
            inserted = True
            
            # Check if the card is blocked
            if blocked:
                print("Your card has been blocked. Contact your branch for further queries.")
                inserted = False
                continue

            # Set PIN if not already set
            if actual_pin is None:
                actual_pin = int(input("Set your new 4-digit PIN: "))
                print("PIN set successfully!")

            # Ask for PIN verification
            pin = int(input("Enter your PIN: "))

            if pin == actual_pin:
                while True:
                    print("\n1. DEPOSIT\n2. WITHDRAWAL\n3. MINI STATEMENT\n4. PIN CHANGE\n5. EXIT")
                    option = int(input("Select an option: "))

                    if option == 1:
                        print("Deposit Money")
                        amount = int(input("Enter the amount (multiples of 100): "))
                        if amount % 100 == 0:
                            balance += amount
                            transactions.append(f"+{amount} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                            print("Cash has been accepted.")
                            print("Available Balance:", balance)
                        else:
                            print("Please enter an amount in multiples of 100.")

                    elif option == 2:
                        print("Withdraw Money")
                        amount = int(input("Enter the amount (multiples of 100): "))
                        if amount > balance:
                            print("Insufficient funds.")
                        elif amount % 100 != 0:
                            print("Please enter an amount in multiples of 100.")
                        else:
                            balance -= amount
                            transactions.append(f"-{amount} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                            print("Cash has been withdrawn.")
                            print("Available Balance:", balance)

                    elif option == 3:
                        print("\nMini Statement")
                        print("Date & Time:", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        print("Last Transactions:")
                        for txn in transactions[-5:]:  # Show last 5 transactions
                            print(txn)
                        print("Current Balance:", balance)

                    elif option == 4:
                        print("Change PIN")
                        old_pin = int(input("Enter old PIN: "))
                        if old_pin == actual_pin:
                            new_pin = int(input("Enter new PIN: "))
                            actual_pin = new_pin
                            print("PIN has been changed successfully.")
                        else:
                            print("Incorrect old PIN.")

                    elif option == 5:
                        print("Thank you! Visit again.")
                        break

            else:
                print("Invalid PIN!")
                attempt += 1
                if attempt >= 2:
                    blocked = True
                    print("Your card has been blocked due to multiple incorrect attempts.")

        else:
            print("Thank you! Visit again.")
             # Exit program

    inserted = False
