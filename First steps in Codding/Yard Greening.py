meters = float(input())

price_meters = 7.61
sum_price = meters * price_meters
discount = sum_price * 0.18
sum_price_discount = sum_price - discount

print(f"The final price is: {sum_price_discount} lv.")
print(f"The discount is: {discount} lv.")