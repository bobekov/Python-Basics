nylon = int(input())
paint = int(input())
thinner = int(input())
hour = int(input())

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5
bags_price = 0.40

nylon += 2
paint += paint * 0.1

material_price = (nylon * nylon_price) + \
                 (paint * paint_price) + \
                 (thinner * thinner_price) + \
                 bags_price
price_for_one_hour = material_price * 0.30
total_price = material_price + (hour * price_for_one_hour)

print(total_price)