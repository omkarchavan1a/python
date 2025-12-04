from tempfile import tempdir


class atm():
    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()
    def menu(self):
        username = input("""
                    hello would you to proceed:
                    1 Enter 1 to create pin
                    2 Entter 2 to deposit
                    3 Enter 3 to withdraw
                    4 Enter 4 to check balance
                    5 Enter 5 to exit
        """)
        if username == "1":
            self.create_pin()
        elif username == "2":
            self.deposit()
        elif username == "3":
            self.withdraw()
        elif username == "4":
            self.check_balance()            
        elif username == "5":
            print("exit")

    def create_pin(self):
        self.pin = input("Enter a pin :")
        print("pin create successfully")

    def deposit(self):
        temp = input("Enter a pin :")
        if temp == self.pin:
            amount = int(input("Enter a amount:"))
            self.balance = self.balance + amount
            print("deposit successfully")
        else:
            print("invalid pin ")     
    
    def withdraw(self):
        temp = input("Enter a pin :")
        if temp == self.pin:
            amount = int(input("Enter a amount:"))
            if amount > self.balance:
                self.balance = self.balance - amount
                print("withdraw successfully")
            else:
                print("insufficient funds")
        else:
            print("invalid pin ")          

    def check_balance(self):
        temp = input("Enter a pin :")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")             