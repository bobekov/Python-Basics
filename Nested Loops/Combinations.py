n = int(input())
sum_num = 0

for num1 in range(0, n+1):
    for num2 in range(0, n+1):
        for num3 in range(0, n+1):
            if num1 + num2 + num3 == n:
                sum_num += 1
print(sum_num)