class Bank:
    bank_name = "Yash International Bank"
    def __init__(self):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@Create Account to Continue@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
        self.name = input("enter name :")
        self.id = int(input("enter id : "))
        self.balance = int(input("Enter opening balance : "))
        self.pin = input("enter pin : ")
        print(f"your acc has been created at {self.bank_name}")
        self.show_menu()

    def show_menu(self):
        while True:
            choice = int(input("""Welcome to Yash International Bank
        1. Show Details
        2. Deposit
        3. Withdraw
        4. Change Pin
        5. Exit 
        Enter Your Choice : """))

            if choice == 1:
                self.show_details()

            elif choice == 2:
                self.deposit()

            elif choice == 3:
                self.withdraw()

            elif choice == 4:
                self.change_pin()

            elif choice == 5:
                break





    def show_details(self):
        data = {"name": self.name,
                "id":self.id,
                "balance":self.balance,
                "pin":self.pin}
        print(data)

    def withdraw(self):
        amt = int(input("Enter amt to withdraw : "))
        if amt>self.balance:
            print("Don't have enough money!")
        self.balance = self.balance- amt
        print("Remaining Balance : ",self.balance)

    def deposit(self):
        amt = int(input("Enter amt to deposit : "))
        self.balance = self.balance + amt
        print("Updated Balance is : ",self.balance)

    def change_pin(self):
        pin = input("enter current pin : ")
        if pin == self.pin:
            new_pin = input("enter new pin : ")
            self.pin = new_pin
        else:
            print("Wrong pin bro! try again")
cus1 = Bank()


