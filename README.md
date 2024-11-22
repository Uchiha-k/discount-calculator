Discount Calculator
A Python program that calculates the final price of an item after applying a discount. It includes detailed validations, bonus discounts for higher percentages, and an interactive user interface.

Features
Core Discount Logic:
Discounts of 20% or higher are applied.
Bonus discounts:
+5% for discounts between 20%-30%.
+10% for discounts above 30%.
Validations:
Ensures prices and discount percentages are non-negative.
Rejects unrealistic discount percentages (e.g., over 100%).
User Interaction:
Interactive loop allows users to calculate discounts for multiple items in one session.
Graceful exit if the user chooses not to continue.
Detailed Output:
Provides a summary of the original price, discount applied, and final price.
Error Handling:
Catches invalid inputs and prompts the user to retry.
How to Run the Program
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/discount-calculator.git
cd discount-calculator
Run the Program: Ensure Python is installed on your system, then execute the program:

bash
Copy code
python discount_calculator.py
Follow the Prompts:

Enter the original price of an item.
Enter the discount percentage.
View the detailed results, including bonus discounts if applicable.
Choose to calculate another discount or exit.
