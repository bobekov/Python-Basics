from math import floor
tournament = int(input())
starting_points = int(input())

won_tournament = 0
gained_points = 0

for _ in range(tournament):
    result = input()

    if result == 'W':
        won_tournament += 1
        gained_points += 2000
    elif result == 'F':
        gained_points += 1200
    elif result == 'SF':
        gained_points += 720


print(f'Final points: {gained_points + starting_points}')
print(f'Average points: {floor(gained_points / tournament)}')
print(f'{won_tournament / tournament * 100:.2f}%')