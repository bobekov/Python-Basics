num1 = int(input())
num2 = int(input())

for number in range(num1, num2 + 1):
    sum_even = 0
    sum_odd = 0

    for index, digit in enumerate(str(number)):
        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)

    if sum_even == sum_odd:
        print(number, end=" ")