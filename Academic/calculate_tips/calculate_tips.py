# Aaron Sage Field
# January 30th, 2025

print("Tip Calculator\n")

# Assume the user will enter valid data

userInput = float(input("Enter Cost of Meal: "))
print("")

# Calculate and display cost of tipping @ 15%, 20%, and 25%

tipOptions = [15,20,25]
for option in tipOptions: # Using a 'for' loop

    # Round results to two decimal places

    tipAmount = round(userInput * (option / 100), 2)
    
    totalAmount = userInput + tipAmount
    print(f"{option}%")
    print(f"Tip Amount: ${tipAmount}")
    print(f"Total Amount: ${totalAmount}")
