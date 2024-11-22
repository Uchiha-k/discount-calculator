def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    Includes tiered bonus discounts for larger percentages.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to be applied.
    
    Returns:
        float: The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount percentage must be non-negative.")
    
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        
        # Add bonus discount for higher discounts
        if 20 <= discount_percent < 30:
            bonus_discount = 0.05 * price
            discount_amount += bonus_discount
        elif discount_percent >= 30:
            bonus_discount = 0.10 * price
            discount_amount += bonus_discount
        
        return price - discount_amount
    else:
        return price

# Main program with looping and detailed outputs
while True:
    try:
        # Input from user
        original_price = float(input("Enter the original price of the item: "))
        discount_percentage = float(input("Enter the discount percentage: "))
        
        # Validation for discount percentage
        if discount_percentage > 100:
            print("Discount percentage cannot exceed 100%. Try again.")
            continue
        
        # Calculate the final price
        final_price = calculate_discount(original_price, discount_percentage)
        
        # Display detailed results
        print("\n--- Discount Calculation Summary ---")
        print(f"Original Price: ${original_price:.2f}")
        print(f"Discount Applied: {discount_percentage:.2f}%")
        if final_price < original_price:
            print(f"Final Price after Discount: ${final_price:.2f}")
        else:
            print(f"No discount applied. Final Price: ${original_price:.2f}")
        print("------------------------------------\n")
        
        # Ask if user wants to continue
        another = input("Do you want to calculate another discount? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thank you for using the Discount Calculator. Goodbye!")
            break
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.\n")
