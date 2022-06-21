#this file in inside bank package
#call module
from customer import Customer
from account import Account

cus1 = Customer()
cus1.new_customer()

cus1_acc = Account()
cus1_acc.open_account(cus1.name,"Saving",'334-201-220-2',500)

print("==== Open Bank Account Detail ====")
print(cus1.cus_info())
print(cus1_acc.display_balance())

#print(cus1.cus_info())