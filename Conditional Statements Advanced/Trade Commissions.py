city = input()
sale_volume = float(input())

commissions = 0
correct_data = True

if city == 'Sofia':
    if 0 <= sale_volume <= 500:
        commissions = sale_volume * 0.05
    elif 500 < sale_volume <= 1000:
        commissions = sale_volume * 0.07
    elif 1000 < sale_volume <= 10000:
        commissions = sale_volume * 0.08
    elif sale_volume > 1000:
        commissions = sale_volume * 0.12
    else:
        correct_data = False

elif city == 'Varna':
    if 0 <= sale_volume <= 500:
        commissions = sale_volume * 0.045
    elif 500 < sale_volume <= 1000:
        commissions = sale_volume * 0.075
    elif 1000 < sale_volume <= 10000:
        commissions = sale_volume * 0.1
    elif sale_volume > 1000:
        commissions = sale_volume * 0.13
    else:
        correct_data = False

elif city == 'Plovdiv':
    if 0 <= sale_volume <= 500:
        commissions = sale_volume * 0.055
    elif 500 < sale_volume <= 1000:
        commissions = sale_volume * 0.08
    elif 1000 < sale_volume <= 10000:
        commissions = sale_volume * 0.12
    elif sale_volume > 1000:
        commissions = sale_volume * 0.145
    else:
        correct_data = False

else:
    correct_data = False


if correct_data:
    print(f"{commissions:.2f}")

else:
    print("error")