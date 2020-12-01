from random import randint

class Account:

    def __init__(self, id:int, balance:float):

        self.id = id
        self.balance = balance

    @property
    def ID(self):
        return self.id

    @property
    def Balance(self):
        return self.balance

    @Balance.setter
    def Balance(self, balance):
        self.balance = balance

    def accStatus(self, ID, Balance):

        print(f"Acc No. {self.ID} Balance: R{self.Balance}")

    def withdraw(self, ID, Balance):

        withdrawn = int(input("How much would you like to withdraw?\n"))

        if Balance < withdrawn:
            print("Insufficient Funds")

        elif Balance >= withdrawn:
            Balance -= withdrawn

    def deposit(self, ID, Balance):

        deposited = int(input("How much would you like to deposit?\n"))

        Balance += deposited

class Savings:

    def __init__(self, yearlyIntrestRate:float):

        self.yearlyIntrestRate = yearlyIntrestRate

    def getMonthlyIntrest(self, monthlyIntrest:float, yearlyIntrestRate, Balance):

        monthlyIntrestRate = yearlyIntrestRate / 12

        monthlyIntrest = Balance * monthlyIntrestRate

        return monthlyIntrest

class ATM(Account):

    def __init__(self, id, balance):
        super().__init__(id, balance)

    def mainMenu(self, id, balance):


        userID = [1234, 2345]

        while True:

            while True:

                inputID = int(input("Please enter your Acc. number\n"))

                if inputID == 1234 or inputID == 2345: # Need to add a better auth method
                    break
                else:
                    print("Acc No. invalid")
            
            while True:

                try:
                    menu = int(input(f"Main Menu\n---------\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit\n"))

                except ValueError:
                    print("INVALID INPUT - Please try again")

                if menu == 1:
                    self.accStatus(id, balance)
                elif menu == 2:
                    self.withdraw(id, balance)
                elif menu == 3:
                    self.deposit(id, balance)
                elif menu == 4:
                    break
                else:
                    print("INVALID INPUT - Please try again")
            
Luca = ATM(1234, 22)
Luca.mainMenu(1234, 22)