count_chicken = int(input())
count_fish = int(input())
count_vegetarian = int(input())

chicken = 10.35
fish = 12.40
vegetarian = 8.15

sum_price = (count_chicken * chicken) +\
              (count_fish * fish) +\
              (count_vegetarian * vegetarian)
desert = (sum_price * 0.2)
delivery = 2.50
final_price = (sum_price + desert + delivery)

print(final_price)