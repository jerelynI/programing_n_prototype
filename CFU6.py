#jerelyn 
#pd1-2
#CFU6

import math
import random

def random_number_calculator():
    random_number = random.randint(1, 100)
    user_input = input("Please enter a number: ")
    try:
        user_number = float(user_input)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    sum_result = random_number + user_number
    difference_result = random_number - user_number
    product_result = random_number * user_number
    if user_number != 0:
        quotient_result = random_number / user_number
        remainder_result = random_number % user_number
    else:
        quotient_result = "undefined (division by zero)"
        remainder_result = "undefined (division by zero)"
    
    square_root_result = math.sqrt(random_number)
    exponentiation_result = math.pow(user_number, random_number)
   
    print("\n--- Results ---")
    print(f"Random Number: {random_number}")
    print(f"User's Number: {user_number}")
    print(f"Sum: {sum_result}")
    print(f"Difference (Random - User): {difference_result}")
    print(f"Product: {product_result}")
    print(f"Quotient (Random / User): {quotient_result}")
    print(f"Remainder (Random % User): {remainder_result}")
    print(f"Square Root of Random: {square_root_result}")
    print(f"User's Number raised to the Power of Random: {exponentiation_result}")


random_number_calculator()
