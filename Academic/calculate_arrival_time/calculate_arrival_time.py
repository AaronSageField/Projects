# Aaron Sage Field
# Arrival Time Estimator
# March 11th, 2025
# Calculates the duration of a trip, in HH:MM granularity, per user input

import sys
from datetime import datetime, timedelta

def displayResults(calculatedResults): # Display the results

    # Corresponding descriptors
    resultDefinitions = ['Hours: ', # [0]
                         'Minutes: ', # [1]
                         'date', # [2]
                         'time'] # [3]
    
    for i, result in enumerate(calculatedResults):
        if i < 2:
            print(f'{resultDefinitions[i]}{calculatedResults[i]}')
        if i > 1:
            print(f'Estimated {resultDefinitions[i]} of arrival: {calculatedResults[i]}')
    print('')

def calculateResults(userVariables): # Calculate and return results

    # Estimated travel time
    calculatedResults = ['0', # Hours [0]
                         '0', # Minutes [1]
                         '0000-00-00', # Date of arrival [2]
                         '00:00 AM'] # Time of arrival [3]

    # Calculate [0],[1]
    exactHours = int(userVariables[2]) / int(userVariables[3])
    calculatedResults[0] = str(int(exactHours))
    exactMinutes = (exactHours - int(calculatedResults[0])) * 60
    calculatedResults[1] = str(int(exactMinutes))

    # Calculate [2],[3]
    departureDatetime = datetime.strptime(f'{userVariables[0]} {userVariables[1]}', '%Y-%m-%d %I:%M %p')
    travelTime = timedelta(hours = int(calculatedResults[0]),
                           minutes = int(calculatedResults[1]))
    arrivalDatetime = departureDatetime + travelTime
    calculatedResults[2] = arrivalDatetime.strftime('%Y-%m-%d')
    calculatedResults[3] = arrivalDatetime.strftime('%I:%M %p')
    return calculatedResults

def userContinues(userVariables): # Calculate & display results on loop
    print('\nEstimated travel time')
    displayResults(calculateResults(userVariables)) # Calculate & display results
    while True: # on loop? (Not written yet)
        userYn = input('Continue? (y/n): ')
        try:
            print('')
            if userYn.strip().lower() == 'y':
                return True
            elif userYn.strip().lower() == 'n':
                return False
        except ValueError:
            pass
        print("Invalid input. Please enter 'y' or 'n'.\n")

def validateInput(userInput, i): # Validate input per prompt
    if i == 0: # Check for valid date of departure [0]
        try:
            datetime.strptime(userInput, '%Y-%m-%d')
        except ValueError:
            print('Please use the (YYYY-MM-DD) format.\n')
            return False
    elif i == 1: # Check for valid time of departure [1]
        try:
            timePart, amPm = userInput.split(" ")
            hour, minute = timePart.split(":")
            if int(hour) < 1 or int(hour) > 12:
                print('Please enter a valid hour (1-12).')
            if int(minute) < 0 or int(minute) >= 60:
                print('Please enter valid minutes (00-59).')
            datetime.strptime(userInput, '%I:%M %p')
        except ValueError:
            print('Please use the (HH:MM AM/PM) format.\n')
            return False
    elif i > 1:
        if userInput.isdigit() == False: # Check if value is an int ([2],[3])
            print('Please enter a non-zero positive integer.\n')
            return False
    return True 

def collectInput(): # Collect, validate, and return userInput as userVariables

    # Necessary inputs..
    userVariables = ['0000-00-00', # Date of departure YYYY-MM-DD [0]
                     '00:00 AM', # Time of departure 12:00 AM/PM [1]
                     '0', # Trip distance in miles [2]
                     '0'] # Miles per hour [3]
    
    # ..and prompts for collection
    userPrompts = ['Enter date of departure (YYYY-MM-DD): ', # [0]
                   'Enter time of departure (HH:MM AM/PM): ', # [1]
                   'Enter miles: ', # [2]
                   'Enter miles per hours: '] # [3]
    
    for i, variable in enumerate(userVariables):
        while True:
            userInput = input(userPrompts[i]) # Collect
            if validateInput(userInput, i): # Validate
                userVariables[i] = userInput
                break          
    return userVariables # Return

def main():
    print('Arrival Time Estimator\n')
    while userContinues(collectInput()): # Collect input and calculate on loop
        pass
    print('Bye!')
    sys.exit()

if __name__ == '__main__':
    main()
    
