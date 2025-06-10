# Aaron Sage Field
# February 6th, 2024
# Calculate sales tax and total after tax using a separate module

# Import Modules
    # Purpose: Enhance visibility for essential functions

import calculations_module

# Function: Get Cost

def input_item_cost():
    
    """Prompt the user to input an item cost and return it as a rounded float."""

    return round(float(input("Cost of item: ")), 2)

# Function: Receive Input

def receive_item_costs():
    
    """Collect item costs from the user until -99 is entered and return the total sum."""

    total = 0.0
    
    print(f"\nENTER ITEMS (ENTER -99 TO END)")
    while True:
        cost = input_item_cost()
        if cost == -99:
            return round(total, 2)
        total += cost

# Function: Get Totals

def calculate_totals():

    """Receive values and calculate totals."""

    total_cost = receive_item_costs()
    sales_tax = calculations_module.calculate_sales_tax(total_cost)
    final_total = calculations_module.calculate_final_total(total_cost)
    return total_cost, sales_tax, final_total

# Function: Master Loop

def master_loop():

    """Handles the transaction loop, displaying results and prompting the user to calculate another bill."""

    total_cost, sales_tax, final_total = calculate_totals()
    print(f"\nTotal:           {total_cost}")
    print(f"Sales tax:       {sales_tax}")
    print(f"Total after tax: {final_total}\n")
    return input("Again? (y/n): ").strip().lower() == 'y' # Assume valid user input

# Function: Main

def main():
    
    """Runs the main program loop, printing the header and footer messages."""

    print("Sales Tax Calculator")
    while master_loop():
        pass

        # Is 'pass' bad practice here?
        # Could use running = true, while running...
        # ...but this is extra work for no point, yes?
        
    print("Thanks, bye!")

# Begin Program

if __name__ == "__main__":
    main()
