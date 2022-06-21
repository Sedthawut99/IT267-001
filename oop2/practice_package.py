from cusorder.customer import Customer
from cusorder.order import Order

#create object customer
cus1 = Customer('Jame','Nontaburi' )
#create order for customer
cus2 = Order('15-06-2022','packed')

#display info
print(f"Order of {cus1.name} on {cus2.date} is {cus2.status}")
