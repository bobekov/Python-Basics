screening_type = input()
rows = int(input())
colums = int(input())

seats = rows * colums
profit = 0

if screening_type == 'Premiere':
    profit = seats * 12
elif screening_type == 'Normal':
    profit = seats * 7.50
elif screening_type == 'Discount':
    profit = seats * 5

print(f"{profit:.2f} leva")