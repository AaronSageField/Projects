# Aaron Sage Field
# Customer Viewer
# March 31st, 2025
# Display customer data from a custom class and per customer ID

    # Sorry if my past use of camelCase was a pain to read..
        # ..I get it now!

class Customer:
    def __init__(self, id, firstName, lastName, company, address, city, state, postalCode):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.postalCode = postalCode

    def return_address(self):
        customer_address = []
        if self.company.strip():
            customer_address.append(self.company.strip())
        customer_address.append(self.address.strip())
        customer_address.append(f'{self.city.strip()}, '
                                f'{self.state.strip()} '
                                f'{self.postalCode.strip()}')
        return '\n'.join(customer_address)
            
        
