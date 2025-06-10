# Aaron Sage Field
# Monthly Sales: REDUX
# March 18th, 2025
# FileIO module

DATA = 'monthly_sales.txt' # Module level constant for the data

def readFile(): # Read the data and return it as a dictionary
    monthlySales = {}
    try:
        with open(DATA, 'r') as dataFile:
            for line in dataFile:
                try: # Ensure file has not been tampered with
                    parts = line.strip().split('\t')
                    if len(parts) != 2:
                        raise ValueError
                    month, salesString = parts
                    try: # Ensure no invalid sales data has been added
                        sales = round(float(salesString), 2)
                        monthlySales[month] = sales
                    except ValueError: # Treat invalid sales as zero
                        monthlySales[month] = 0
                except ValueError:
                    print('File is corrupted or does not meet expected format.')
                    print('Please replace monthly_sales.txt and try again.')
                    return {}
        return monthlySales # Return dictionary
    except FileNotFoundError:
        print('monthly_sales.txt could not be found. Please replace the file.\n')
        return {} # Return empty dictionary to reflect "empty" data
    except Exception as e:
        print('Error when attempting to read monthly_sales.txt\n')
        print(type(e), e)
        return {} # Return empty dictionary to reflect "empty" data

def writeFile(monthlySales): # Overwrite the file with the new dictionary
    try:
        with open(DATA, 'w') as dataFile:
            for month, sales in monthlySales.items():
                dataFile.write(f'{month}\t{sales}\n')
        return True
    except Exception as e:
        print('Error when attempting to write monthly_sales.txt\n')
        print(type(e), e)
        return False
