account_balance=5000
your_pin=1234

def transaction ():
    name=input("Enter name to proceed")
    print("WELCOME", name)
    pin=int(input("Enter pin to proceed"))
    if pin==your_pin:
        withdraw=int(input("Enter amount to withdraw"))
        if (account_balance > withdraw):
            Total= account_balance-withdraw
            print("Transaction successful ,your new balance is", Total)
        else:
            print("Insufficient Balance")          
    else:
      print("Please enter correct pin & try again")
transaction ()