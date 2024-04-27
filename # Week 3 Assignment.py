# Week 3 Assignment

def calculate_discount(price, discount_percent):
     
    if (discount_percent >= 0.20):
        final_price = price - (discount_percent * price)
        return final_price
    else:
        return price
    
original_price = float(input("Enter the initial price: "))
discount_percentage = float(input('Percentage discount offered: '))

final_price = calculate_discount(original_price, discount_percentage)
print("Final price: ", final_price)
print("Original Price: ", original_price)