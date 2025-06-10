# Aaron Sage Field
# Customer Employee Creator
# April 8th, 2025
# An Object-Oriented Program for Customer-Data Entry

import company_objects
import sys

def display_person(person_object): # Display the Customer or Employee
    if isinstance(person_object, company_objects.Customer):
        print('\nCUSTOMER')
        print(f"{'Full name:':<12}{person_object.return_name()}")
        print(f"{'Email:':<12}{person_object.email}")
        print(f"{'Number:':<12}{person_object.number}\n")
    else:
        print('\nEMPLOYEE')
        print(f"{'Full name:':<12}{person_object.return_name()}")
        print(f"{'Email:':<12}{person_object.email}")
        print(f"{'SSN:':<12}{person_object.ssn}\n")

def user_continues():
    while True:
        user_command = input('Continue? (y/n): ').strip().lower()
        if user_command == 'y':
            print('')
            return True
        elif user_command == 'n':
            print('\nBye!\n')
            sys.exit()
        print('Invalid command.\n')

def main():
    print('Customer/Employee Data Entry\n')

    # Create an object from data entry and store as a single variable
    while True:
        user_command = input('Customer or employee? (c/e): ').strip().lower()
        if user_command != 'c' and user_command != 'e':
            print('Invalid command.\n')
        else:
            person = {
                'first_name': '',
                'last_name': '',
                'email': ''
                }
            print('\nDATA ENTRY')
            person['first_name'] = input('First name: ').strip()
            person['last_name'] = input('Last name: ').strip()

            # Validate email for (potentially local) domain
            try:
                person_email = input('Email: ').strip()
                if '@' not in person_email:
                    raise ValueError
                person['email'] = person_email
            except ValueError:
                print('\nEmail must contain a domain.\n')
                if user_continues(): # Provide option to exit cleanly
                    continue

            # Validate 'M12345' format
            if user_command == 'c': 
                person_number = input('Number: ').strip()
                try: 
                    validate_number = int(person_number[1:])
                    if '.' in person_number or 'M' not in person_number[0]:
                        raise ValueError
                    elif len(person_number) > 6:
                        raise ValueError
                    person['number'] = person_number
                except ValueError:
                    print('\nInvalid Customer Number.\n')
                    if user_continues():
                        continue
                person_object = company_objects.Customer(person['first_name'],
                                                         person['last_name'],
                                                         person['email'],
                                                         person['number'])

            # Validate '123-45-6789' format
            elif user_command == 'e': 
                person_ssn = input('SSN: ').strip()
                try: 
                    if len(person_ssn) != 11 or person_ssn[3] != '-' or person_ssn[6] != '-':
                        raise ValueError
                    validate_ssn = int(person_ssn.replace('-', ''))
                    person['ssn'] = person_ssn
                except ValueError:
                    print('\nInvalid Social Security Number.\n')
                    if user_continues():
                        continue
                person_object = company_objects.Employee(person['first_name'],
                                                         person['last_name'],
                                                         person['email'],
                                                         person['ssn'])

            # Display entry and continue(?)
            display_person(person_object)
            if user_continues():
                continue
                    
if __name__ in '__main__':
    main()
