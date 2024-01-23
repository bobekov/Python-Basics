days_stays = int(input())
room_type = input()
rating = input()

room_one_person = 18
apartment = 25
president_apartment = 35

price = 0

if room_type == 'room for one person':
    price = ((days_stays - 1) * room_one_person)

elif room_type == 'apartment':
    if days_stays < 10:
        price = ((days_stays - 1) * apartment) * 0.75
    elif 10 <= days_stays <= 15:
        price = ((days_stays - 1) * apartment) * 0.65
    elif days_stays > 15:
        price = ((days_stays - 1) * apartment) * 0.5

elif room_type == 'president apartment':
    if days_stays < 10:
        price = ((days_stays - 1) * president_apartment) * 0.90
    elif 10 <= days_stays <= 15:
        price = ((days_stays - 1) * president_apartment) * 0.85
    elif days_stays > 15:
        price = ((days_stays - 1) * president_apartment) * 0.8

if rating == 'positive':
    price = price + (price * 0.25)

elif rating == 'negative':
    price = price - (price * 0.1)


print(f"{price:.2f}")