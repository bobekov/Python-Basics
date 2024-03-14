while True:
    destination = input()

    if destination == 'End':
        break

    budget = float(input())
    sum_money = 0

    while budget > sum_money:
        sum_money += float(input())

    print(f'Going to {destination}!')