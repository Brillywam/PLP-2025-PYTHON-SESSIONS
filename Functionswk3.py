def calculate_discount(price, discount_percent):
    """Calculate the discount amount based on the price and discount percentage."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
# User Prompt for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))
#calculate final price
final_price = calculate_discount(original_price, discount_percentage)
#print result
if discount_percentage >= 20:
    print(f"The final price after a discount of {discount_percentage}% is: ${final_price}")
else:
    print(f"No discount applied. The price remains: ${original_price}")