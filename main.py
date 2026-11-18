
from Current_Account import Current_Account
from Simple_Account import Simple_Account
from Bank_Account import Bank_Account
from Savings_Account import Savings_Account


# creating an object of class simple account
# sAccount1 = Simple_Account()
# sAccount1.method1()

# creating an object of class Bank account

# bankAcc1 = Bank_Account()
# bankAcc1.deposite_amount()




#create an object of current account
cal = Current_Account()
cal.dummy()
cal. deposite(1000)
#print(f"balance amount is :{cal._Bank_Account__balance}")
cal.display_balance()

# Current_Account = Current_Account()
# Current_Account.dummy()


cal.deposite(2000)
cal.display_balance()

cal.withrawal(1000)
cal.display_balance()


print("*****************************************************")


savingsAcc1 = Savings_Account()
savingsAcc1.duplicate()

savingsAcc1.deposite(1000)
savingsAcc1.display_balance()

savingsAcc1.withrawal(500)
savingsAcc1.display_balance()

savingsAcc1.calculate_interest()
print(f"Interest earned: {savingsAcc1.calculate_interest()}")

print("hello world")

print("hi dear")

