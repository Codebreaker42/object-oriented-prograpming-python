class Atm:
    # constructor
    def __init__(self):
        print("welcome to our service")
        self.pin=0
        self.balance=0

    # menu
    def menu(self):
        user_input=int(input("""
              hello how would you proceed 
              1.Enter 1 for create pin
              2.Enter 2 for deposit 
              3.Enter 3 to withdraw
              4.Enter 4 to check balance
              5.Enter 5 to exit
              """))
        print(user_input)
        if user_input==1:
            temp_pin=int(input("Set your pin"))
            self.pin=temp_pin
            print("Pin Set Successfully")
        elif user_input==2:
            print("Deposit")
            self.deposit()
        elif user_input==3:
            print('Withdraw')
            self.withdraw()
        elif user_input==4:
            print('balance')
            self.check_balance()
        else:
            print("thanks for using our service")

    # function for creating pin
    def create_pin(self):
        self.pin=input("Enter your pin")
        print("pin set successfully")

    # function for deposit
    def deposit(self):
        temp_pin=int(input("Enter pin for gaining access into system"))
        if temp_pin==self.pin:
            print("Correct Pin Now you can proceed")
            amt=int(input('Enter amount to deposit'))
            self.balance=self.balance+amt
            print("Deposit Successfully")
        else:
            print("Incorrect Pin")

    # function for withdraw
    def withdraw(self):
        temp_pin=int(input("Enter pin for gaining access into system"))
        if temp_pin==self.pin:
            print("Correct Pin Now you can proceed")
            amt=int(input('Enter amount to withdrawl'))
            if self.balance>=amt:
                self.balance=self.balance-amt
                print("Withdraw Successfully")
            else:
                print("Insufficient Balance")
        else:
            print("Incorrect Pin")

    # function for check balance
    def check_balance(self):
        temp_pin=int(input("Enter pin for gaining access into system"))
        if temp_pin==self.pin:
            print("Correct Pin Now you can proceed")
            print(f"balance = {self.balance}")
        else:
            print("Invalid Pin")

# making object
sbi=Atm()
#calling menu function
sbi.menu()
sbi.deposit()
sbi.check_balance()
sbi.withdraw()
sbi.check_balance()