# Aaron Sage Field
# Customer Viewer
# March 31st, 2025
# Display customer data from a custom class and per customer ID

import csv
import sys
from CustomerModule import Customer

def list_customers():
    data = 'customers.csv'
    customer_matrix = []
    try:
        with open(data, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                customer_object = Customer(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7]
                )
                customer_matrix.append(customer_object)
        del customer_matrix[0]
        return customer_matrix
    except FileNotFoundError:
        print(f'{data} is missing from your directory.\n')
        sys.exit()
    except Exception as e:
        print(f'Unexpected error when reading {data}:\n{type(e)}\n{e}\n')
        sys.exit()

def find_customer(user_input):
    customers = list_customers()
    for customer in customers:
        if customer.id == user_input:
            print(f'\n{customer.return_address()}\n')
            return True
    return False

def main():
    print('Customer Viewer\nEnter the customer ID to view the customer address')
    while True: # Collect ID
        user_input = input('\nEnter customer ID: ').strip()
        if not find_customer(user_input):
            print('\nNo customer with that ID.')
            continue
        while True: # Continue?
            user_input = input('Continue? (y/n): ').strip().lower()
            if user_input == 'n':
                print('\nBye!\n')
                sys.exit()
            elif user_input != 'y':
                print('\nInvalid response.\n')
                continue
            break
   
if __name__ in '__main__':
    main()
