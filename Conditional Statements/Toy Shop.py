price_excursion = float(input())
puzzles_count = int(input())
doll_count = int(input())
bear_count = int(input())
minions_count = int(input())
truck_count = int(input())

puzzles_price = 2.60
doll_price = 3
bear_price = 4.10
minions_price = 8.20
truck_price = 2

sum_toy = puzzles_count + \
          doll_count + \
          bear_count + \
          minions_count + \
          truck_count
sum_toy_price = (puzzles_count * puzzles_price) + \
                (doll_count * doll_price) + \
                (bear_count * bear_price) + \
                (minions_count * minions_price) + \
                (truck_count * truck_price)

if sum_toy >= 50:
    sum_toy_price -= sum_toy_price * 0.25

sum_toy_price -= sum_toy_price * 0.1

if sum_toy_price >= price_excursion:
    print(f"Yes! {sum_toy_price - price_excursion:.2f} lv left.")
else:
    print(f"Not enough money! {price_excursion - sum_toy_price:.2f} lv needed.")