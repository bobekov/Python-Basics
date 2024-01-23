budget = float(input())
statistics = int(input())
price_clothing_statistics = float(input())

decor = budget * 0.1

if statistics > 150:
    price_clothing_statistics -= price_clothing_statistics * 0.1

our_budget = (statistics * price_clothing_statistics) + decor

if our_budget <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - our_budget:.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {our_budget - budget:.2f} leva more.")