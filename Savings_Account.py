#savings account

from Bank_Account import Bank_Account


class Savings_Account(Bank_Account):
    # def __init__(self,balance):
    #     super().__init__(balance )

    def duplicate(self):
         pass
    
    def calculate_interest(self):
        # fetching the balance first and calculate the interest
        interest = (self.get_balance()) * 0.05                               # Example interest calculation
        return interest
