budget = float(input())
count_videocard = int(input())
count_procesor = int(input())
count_rammemmory = int(input())

videocard_price = 250
sum_videocard = count_videocard * videocard_price

procesor_price = sum_videocard * 0.35
sum_procesor = count_procesor * procesor_price

rammemmory_price = sum_videocard * 0.1
sum_rammemmory = count_rammemmory * rammemmory_price

sum_price = sum_videocard + sum_procesor + sum_rammemmory

if count_videocard > count_procesor:
    sum_price *= 0.85

if sum_price <= budget:
    print(f"You have {budget - sum_price:.2f} leva left!")

else:
    print(f"Not enough money! You need {sum_price - budget:.2f} leva more!")