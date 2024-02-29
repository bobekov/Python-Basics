money_excursion = float(input())
available_money = float(input())
days = 0
total_days = 0

while days < 5:
    action = input()
    amount = float(input())
    total_days += 1

    if action == 'spend':
        available_money = available_money - amount if available_money > amount else 0
        days += 1
    else:
        available_money += amount
        days = 0

    if available_money >= money_excursion:
        print(f'You saved the money for {total_days} days.')
        break

else:
    print("You can't save the money.")
    print(f'{total_days}')