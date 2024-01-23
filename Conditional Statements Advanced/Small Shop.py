product = input()
city = input()
price = float(input())

sum_price = 0

if city == 'Sofia':
    if product == 'coffee':
        sum_price = price * 0.50
    elif product == 'water':
        sum_price = price * 0.80
    elif product == 'beer':
        sum_price = price * 1.20
    elif product == 'sweets':
        sum_price = price * 1.45
    elif product == 'peanuts':
        sum_price = price * 1.60

elif city == 'Plovdiv':
    if product == 'coffee':
        sum_price = price * 0.40
    elif product == 'water':
        sum_price = price * 0.70
    elif product == 'beer':
        sum_price = price * 1.15
    elif product == 'sweets':
        sum_price = price * 1.30
    elif product == 'peanuts':
        sum_price = price * 1.50

elif city == 'Varna':
    if product == 'coffee':
        sum_price = price * 0.45
    elif product == 'water':
        sum_price = price * 0.70
    elif product == 'beer':
        sum_price = price * 1.10
    elif product == 'sweets':
        sum_price = price * 1.35
    elif product == 'peanuts':
        sum_price = price * 1.55

print(sum_price)
