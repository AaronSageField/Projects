# Aaron Sage Field
# Monthly Sales
# March 18th, 2025
# View and edit sales amounts for each month of the year w/ a dictionary

import sys
import FileIO as readWrite

def sigFig(yearlyTotal): # Checks if a value has only 1 sigfig
    numberString = f'{yearlyTotal:.2f}'
    integerPart, decimalPart = numberString.split('.')
    if decimalPart[0] != '0' and decimalPart[1] == '0':
        return True
    return False

def viewAnnual(monthlySales): # View yearlyTotal and monthlyAverage
    displayValues = {   # Description: value
        'Yearly total:': 0,
        'Monthly average:': 0
        }
    yearlyTotal = 0 # Calculate yearlyTotal and assign appropriately
    for month in monthlySales: 
        yearlyTotal += monthlySales[month]
    displayValues['Yearly total:'] = yearlyTotal

    # Calculate monthlyAverage and assign appropriately
    displayValues['Monthly average:'] = yearlyTotal / 12

    for key, value in displayValues.items():
        if value % 1 == 0:
            displayValue = int(value)
            print(f'{key:<16}{displayValue:>14,}')
        elif sigFig(value):
            print(f'{key:<16}{value:>14,.1f}')
        else:
            print(f'{key:<16}{value:>14,.2f}')
    print('')

def editMonth(monthlySales): # Edit sales per key
    validInput = False # Assume invalid input
    userInput = input('\nThree-letter Month: ').strip().lower()
    for month in monthlySales: # Check if user input corresponds to a key
        if month.lower() == userInput:
            newValue = input('Sales Amount: ') # If so, collect value
            try:
                newValue = round(float(newValue), 2)
            except ValueError:
                print('Invalid input for Sales Amount.\n')
                return
            monthlySales[month] = newValue
            validInput = True # Signal successful operation
    if not validInput: # Take action per validInput signal
        print('Invalid three-letter month.\n')
    else:
        readWrite.writeFile(monthlySales)
        print('')

def viewMonth(monthlySales): # View sales per key
    userInput = input('Three-letter Month: ').strip().lower()
    for month in monthlySales: # Check if user input corresponds to a key..
        if month.lower() == userInput: # ..and print the key value
                print(f'Sales amount for {month} is {monthlySales[month]:.2f}.\n')
                return
    print('Invalid three-letter month.\n')

def displayCommands(commandMenu):

    # To accomdate the potential introduction of new commands
    longestKey = max(len(key) for key in commandMenu) + 1

    print('COMMAND MENU')
    for command, (function, description) in commandMenu.items():
        print(f'{command:<{longestKey}}{description}')
    print(f'{"exit":<{longestKey}}- Exit program\n')

def collectInput(commandMenu, monthlySales):
    while True:
        monthlySales = readWrite.readFile() # Update before passing to command        
        userInput = input('Command: ').strip().lower()
        if userInput in commandMenu:
            commandMenu[userInput][0](monthlySales)
            continue
        elif userInput == 'exit':
            print('Bye!')
            sys.exit()
        print('Invalid command.\n')
        displayCommands(commandMenu)

def main():
    monthlySales = readWrite.readFile() # Initialize sales dictionary

    # Do not allow program to continue if FileNotFound or invalid format
    if not monthlySales:
        sys.exit()
    
    commandMenu = {         # Command: (function, description)
        'view': (viewMonth, '- View sales for specified month'),
        'edit': (editMonth, '- Edit sales for specified month'),
        'totals': (viewAnnual, '- View sales summary for year'),
        }
    print('Monthly Sales program\n')
    displayCommands(commandMenu) # Print the command menu
    collectInput(commandMenu, monthlySales) # Accept valid user command and execute

if __name__ in '__main__':
    main()
