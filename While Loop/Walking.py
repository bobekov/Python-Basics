goal = 10_000
sum_steps = 0

while goal > sum_steps:
    steps = input()

    if steps == 'Going home':
        sum_steps += int(input())
        break

    sum_steps += int(steps)

if sum_steps >= goal:
    print(f'Goal reached! Good job!')
    print(f'{sum_steps - goal} steps over the goal!')

else:
    print(f'{goal - sum_steps} more steps to reach goal.')