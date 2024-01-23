month = input()
overnight = int(input())

studio = 0
flat = 0

if month == 'May' or month == 'October':
    studio = overnight * 50
    if 7 < overnight <= 14:
        studio *= 0.95
    elif overnight > 14:
        studio *= 0.70
    flat = overnight * 65

elif month == 'June' or month == 'September':
    studio = overnight * 75.20
    if overnight > 14:
        studio *= 0.80
    flat = overnight * 68.70

elif month == 'July' or month == 'August':
    studio = overnight * 76
    flat = overnight * 77

if overnight > 14:
    flat *= 0.90

print(f"Apartment: {flat:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")