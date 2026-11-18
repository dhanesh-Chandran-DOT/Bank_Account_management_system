#******************************


from abc import ABC, abstractmethod

# creating a class as an bstract class

class Bank_Account(ABC):

    # constructor of the class
    def __init__(self):
        self.__balance = 0
    # creating an abstract method

    @abstractmethod
    def calculate_interest(self):
        pass

    property
    def balance(self):
        return self.__balance

    # @balance.setter
    def balance(self,value):
        if value <= 0:
            raise ValueError("balance cannot be negative")
        self.__balance = value

    # it displays the balance amount
    def display_balance(self):
        print(f"your balance amount is {self.__balance}")
        
    # returns the balance amount
    def get_balance(self):
        return self.__balance


    def deposite(self,dep_amount):
        if dep_amount <= 0:
            raise ValueError("deposite amount cannot be negative")
        self.__balance = self.__balance +  dep_amount

    def withrawal(self,with_amount):
        if with_amount <= 0:
            raise ValueError("withdrawal amount cannot be negative")
        elif with_amount > self.__balance:
            raise ValueError("withdrawal amount cannot be greater than balance")
        self.__balance = self.__balance - with_amount

    


        
        





    

