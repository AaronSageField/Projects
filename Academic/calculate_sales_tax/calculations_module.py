# Aaron Sage Field
# February 6th, 2024
        
"""
This module provides functions to calculate sales tax and the total amount after tax.

Constants:
SALES_TAX (float): Sales tax as a percentage. Default value: 6%
"""

# Declare global constants
    # Purpose: To provide visibility as to global variables utilized

SALES_TAX = 0.06
    
# Function: Calc Sales Tax
    # Purpose: Calculate sales tax for a given total cost

def calculate_sales_tax(total_cost):

    """Return the sales tax for a given total cost; rounded to 2."""

    return round(total_cost * SALES_TAX, 2)

# Function: Calc Total After Tax
    # Purpose: Calculate total amount

def calculate_final_total(total_cost):

    """Return the sum of: a value; and sales tax per calculate_sales_tax"""

    return round(total_cost + calculate_sales_tax(total_cost), 2)
