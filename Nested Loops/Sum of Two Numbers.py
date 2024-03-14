first_interval = int(input())
last_interval = int(input())
magic_number = int(input())

combinations = 0
break_condition = False

for num1 in range(first_interval, last_interval+1):
    for num2 in range(first_interval, last_interval+1):
        combinations += 1

        if num1 + num2 == magic_number:
            break_condition = True
            print(f'Combination N:{combinations} ({num1} + {num2} = {magic_number})')
            break

    if break_condition:
        break

if not break_condition:
    print(f'{combinations} combinations - neither equals {magic_number}')