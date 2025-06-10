# Aaron Sage Field
# Customer Employee Creator
# April 8th, 2025
# An Object-Oriented Program for Customer-Data Entry

# Create a Person class
    # Attributes: First name, last name, email address
    # Methods: Return full name

class Person:
    def __init__(self, first_name = '', last_name = '', email = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def return_name(self):
        name = self.first_name + ' ' + self.last_name
        return name

# Create a Customer subclass
    # Add attribute: Customer Number

class Customer(Person):
    def __init__(self, first_name = '', last_name = '', email = '', number = ''):
        Person.__init__(self, first_name, last_name, email)
        self.number = number

# Create an Employee subclass
    # Add attribute: Social Security Number

class Employee(Person):
    def __init__(self, first_name = '', last_name = '', email = '', ssn = ''):
        Person.__init__(self, first_name, last_name, email)
        self.ssn = ssn
