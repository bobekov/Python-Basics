n = int(input())

left_sum = 0
right_sum = 0

for i in range(0, n):
    left_number = int(input())
    left_sum += left_number

for i in range(0, n):
    right_number = int(input())
    right_sum += right_number

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(right_sum - left_sum)}')