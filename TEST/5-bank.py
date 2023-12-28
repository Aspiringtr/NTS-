customer_details = []
for i in range(5):
    name = input("Enter customer name: ")
    account_number = input("Enter account number: ")
    balance = float(input("Enter account balance: "))
    customer_details.append((name, account_number, balance))
print("\nCustomers with balance greater than or equal to 10000:")
for customer in customer_details:
    name, account_number, balance = customer
    if balance >= 10000:
        print(f"Name: {name}, Account Number: {account_number}, Balance: {balance}")
