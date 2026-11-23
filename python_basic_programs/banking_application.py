########################## Banking Application ######################################33
accounts ={}
    

while True:
    print("Welcome to the Banking application")
    print("========Banking Menu============")
    print("1.Create Account ")
    print("2.Deposite ")
    print("3.Withdraw ")
    print("4.Check Balance ")
    print("5.Transfer money ")
    print("6.Show All Accounts ")
    print("7.Exit ")

    choice = int(input("Enter your choice"))

    if choice == 1:
        account_number = input("Enter Account Number: ")

        if account_number in accounts:
            print("Account already exists.")

        else:
            name = input("Enter Customer Name: ")
            balance = float(input("Enter Initial Balance: "))

            if balance < 0:
                print("Balance cannot be negative.")
            else:
                accounts[account_number] = {
                    "Name": name,
                    "Balance": balance
                }

                print("Account created successfully.",accounts)

    elif choice==7:
         break

else:
        print("Invalid choice. Please try again.")

