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

    def setValue(self, id, balance):

        id = randint(1000, 9999)
        balance = randint(0.0, 10000000.0)

    def accStatus(self, id, balance):

        return f"Acc No. {self.id} Balance: R{self.balance}"

    def withdraw(self, id, balance):

        withdrawn = int(input("How much would you like to withdraw?\n"))

        balance -= withdrawn

    def deposit(self, id, balance):

        deposited = int(input("How much would you like to deposit?\n"))

        balance -= deposited

    class Savings:

        def __init__(self, yearlyIntrestRate:float):

            self.yearlyIntrestRate = yearlyIntrestRate

        def getMonthlyIntrest(self, monthlyIntrest:float, yearlyIntrestRate, Balance):

            monthlyIntrestRate = yearlyIntrestRate / 12

            monthlyIntrest = Balance * monthlyIntrestRate

            return monthlyIntrest

class ATM:

    def mainMenu(self, id, balance):

        account = Account(id, balance)

        userID = [1234, 2345]

        while True:

            while True:

                inputID = int(input("Please enter your Acc. number"))

                if inputID == userID[1] or inputID == userID[2]:
                    break
                else:
                    print("Acc No. invalid")
            
            while True:

                menu = int(input(f"Main Menu\n---------\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit\n"))

                if menu == 1:
                    account.accStatus(id, balance)
                elif menu == 2:
                    account.withdraw(id, balance)
                elif menu == 3:
                    account.deposit(id, balance)
                elif menu == 4:
                    break
                else:
                    print("INVALID INPUT - Please try again")
            
Luca = mainMenu(1234, 22)




