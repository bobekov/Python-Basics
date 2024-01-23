type_flowers = input()
sum_flowers = int(input())
budget = int(input())

Roses = 5
Dahlias = 3.80
Tulips = 2.80
Narcissus = 3
Gladiolus = 2.50

price = 0

if type_flowers == 'Roses':
    price = sum_flowers * Roses

    if sum_flowers > 80:
        price *= 0.90

elif type_flowers == 'Dahlias':
    price = sum_flowers * Dahlias

    if sum_flowers > 90:
        price *= 0.85

elif type_flowers == 'Tulips':
    price = sum_flowers * Tulips

    if sum_flowers > 80:
        price *= 0.85

elif type_flowers == 'Narcissus':
    price = sum_flowers * Narcissus

    if sum_flowers < 120:
        price *= 1.15

elif type_flowers == 'Gladiolus':
    price = sum_flowers * Gladiolus

    if sum_flowers < 80:
        price *= 1.20

if price <= budget:
    print(f"Hey, you have a great garden with {sum_flowers} {type_flowers} and {budget - price:.2f} leva left.")

else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")