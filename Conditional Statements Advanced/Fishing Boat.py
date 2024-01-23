budget = int(input())
season = input()
sum_fisher = int(input())

price = 0

if season == 'Spring':
    price = 3000
elif season == 'Winter':
    price = 2600
else:
    price = 4200

if sum_fisher <= 6:
    price *= 0.90
elif 7 <= sum_fisher <= 11:
    price *= 0.85
else:
    price *= 0.75

if sum_fisher % 2 == 0 and season != "Autumn":
    price *= 0.95

if price <= budget:
    print(f"Yes! You have {budget - price:.2f} leva left.")

else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")


